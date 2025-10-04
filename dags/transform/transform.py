import psycopg2
import pandas as pd
from logger import setup_logger
from thefuzz import process , fuzz
from mapping import job_roles_mapping, programming_languages_mapping, required_skills_mapping, education_mapping, position_mapping,location_mapping
import re
from unidecode import unidecode
logger = setup_logger("transform")

def clean_text(text :str ) -> str:
    if pd.isna(text):
        return ""
    return text.lower().strip()
#====================================================================================================
def normalize_title(title : str):
    title = clean_text(title)
    best_match = None
    best_score = 0
    for role, potential_match_list in job_roles_mapping.items():
        match,score = process.extractOne(title,potential_match_list)
        if (score > best_score):
            best_score = score
            best_match = role
    return best_match if best_score >= 65 else "other technical job"
#====================================================================================================
def get_programming_languages(requirement : str) -> list[str]:
    languages = set()
    requirement = clean_text(requirement)
    requirement = re.sub(r'[^a-zA-Z0-9+#]', ' ', requirement)
    for language in programming_languages_mapping:
        pattern = rf"\b{re.escape(language.lower())}\b"
        if re.search(pattern, requirement):
            languages.add(language)
    return list(languages)

#====================================================================================================
def get_required_skills(requirement : str) -> list[str]:
    required_skills = set()
    requirement = clean_text(requirement)
    requirement = re.sub(r'[^a-zA-Z0-9+#]', ' ', requirement)
    for skills in required_skills_mapping:
        pattern = rf"\b{re.escape(skills.lower())}\b"
        if re.search(pattern, requirement):
            required_skills.add(skills)
    return list(required_skills)
#====================================================================================================
def normalize_education(education : str) -> str:
    education = clean_text(education)
    for level, pattern in education_mapping.items():
        pattern = rf"\b{pattern}\b"
        if re.search(pattern,education):
            return level
    return 'No requirement'
#====================================================================================================
def normalize_position(pos: str) -> str:
    pos = clean_text(pos)
    if pos == "" :
        return None
    for eng, viet in position_mapping.items():
        pattern = rf"\b{re.escape(viet.lower())}\b"
        if re.search(pattern, pos):
            return eng
    return None
#====================================================================================================
def normalize_location(location : str) -> str:
    location = clean_text(location)
    location = unidecode(str(location).lower())
    locations = []
    for place in location_mapping:
        pattern = rf"\b{re.escape(place)}\b"
        if re.search(pattern,location):
            locations.append(place)
    return locations
#====================================================================================================
def extract_quantity(quantity : pd.Series):
    return quantity.str.extract(r"(\d+)")
#====================================================================================================
def extract_unit(salary : str) -> str:
    salary = clean_text(salary)
    if "triệu" in salary:
        return "VND"
    elif "usd" in salary:
        return "USD"
    else:
        return None
#====================================================================================================
def extract_min_max_from_salary(salary : str) -> tuple:
    EXCHANGE_RATE = 26500
    salary = clean_text(salary)
    salary = re.sub("[,.]","",salary)
    if salary == "":
        return (None,None)
    if 'từ' in salary:
        match = re.search(r"từ\s+(\d+)",salary)
        if match:
            unit = extract_unit(salary)
            if unit == "USD":
                return (float(match.group(1)),None)
            elif unit == 'VND':
                return (float(match.group(1))*1000000/EXCHANGE_RATE,None)
        
    elif 'tới' in salary:
        match = re.search(r"tới\s+(\d+)",salary)
        if match:
            unit = extract_unit(salary)
            if unit == "USD":
                return (None,float(match.group(1)))
            elif unit == "VND":
                return (None, float(match.group(1))*1000000/EXCHANGE_RATE)
    elif '-' in salary:
        match = re.search(r"(\d+)\s*-\s*(\d+)",salary)
        if match:
            unit = extract_unit(salary)
            if unit == 'USD':
                return (float(match.group(1)),float(match.group(2)))
            if unit == 'VND':
                return (float(match.group(1))*1000000/EXCHANGE_RATE,float(match.group(2))*1000000/EXCHANGE_RATE)
#====================================================================================================
def extract_year(experience : pd.Series) :
    experience = experience.apply(clean_text)
    year = experience.str.extract(r"(\d+)")
    year[experience.str.contains("không yêu cầu", na = False)]=0
    return year
#====================================================================================================
def normalize_company(company : str):
    company = clean_text(company)
    if company == "":
        return None
    return company
#====================================================================================================
def convert_type(df: pd.DataFrame) -> pd.DataFrame:
    df['title'] = df['title'].astype("string")
    df['education'] = df['education'].astype('string')
    df['position'] = df['position'].astype('string')
    df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce').astype("Int64")
    df['experience'] = pd.to_numeric(df['experience'], errors='coerce').astype("Int64")
    df['company'] = df['company'].astype("string")
    df['min_salary'] = pd.to_numeric(df['min_salary'], errors='coerce').astype("Float64").round(1)
    df['max_salary'] = pd.to_numeric(df['max_salary'], errors='coerce').astype("Float64").round(1)
    return df


#====================================================================================================

def transform_topcv(df : pd.DataFrame) -> pd.DataFrame:
    """Transfrom topcv dataframe"""
    try:
        logger.info ("Start transforming TopCV dataframe")

        logger.info("Normalizing title...")
        df['title'] = df['title'].apply(normalize_title)

        logger.info("Normalizing company...")
        df['company'] = df['company'].apply(normalize_company)
        
        logger.info("Merging requirement and description...")
        df['full'] = df['requirement'].fillna('') + ' ' + df['description'].fillna('')

        logger.info("Extracting programming languages...")
        df['programming_languages'] = df['full'].apply(get_programming_languages)

        logger.info("Extracting required skills...")
        df['required_skills'] = df['full'].apply(get_required_skills)

        logger.info("Normalizing education...")
        df['education'] = df['education'].apply(normalize_education)

        logger.info("Normalizing position...")
        df['position'] = df['position'].apply(normalize_position)

        logger.info("Normalizing location...")
        df['locations'] = df['location'].apply(normalize_location)

        logger.info("Extracting quanity...")
        df['quantity'] = extract_quantity(df['quantity'])

        logger.info("Extracting experience...")
        df['experience'] = extract_year(df['experience'])

        logger.info("Extracting salary ranges")
        df[['min_salary','max_salary']] = df['salary'].apply(extract_min_max_from_salary).apply(pd.Series)

        logger.info("Converting datatype...")
        df = convert_type(df)

        logger.info("Handling NULL...")
        df = df.where(pd.notnull(df),None)
        logger.info("Transformed successfully")
    except Exception as e:
        logger.error(f"Error transforming: {e}")
    return df[['title','programming_languages','required_skills','education','experience','position','locations','quantity','min_salary','max_salary','company']]
if __name__ == '__main__':
    df = pd.read_csv("dataset/topcv_bronze_raw.csv")
    df = transform_topcv(df)
    pd.set_option('display.max_rows', None)   
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_colwidth', None) 
    print(df)
