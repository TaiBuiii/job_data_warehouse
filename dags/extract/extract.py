import requests
from bs4 import BeautifulSoup
from logger import setup_logger
import random, time
import re

logger = setup_logger("extract")

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64; rv:117.0) Gecko/20100101 Firefox/117.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
]

def get_headers():
    """Sinh headers ngẫu nhiên để tránh bị block"""
    return {
        "User-Agent": random.choice(USER_AGENTS),
        "Accept-Language": "vi-VN,vi;q=0.9,en;q=0.8",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Connection": "keep-alive",
        "Referer": "https://www.topcv.vn/tim-viec-lam-cong-nghe-thong-tin-cr257",
    }

def fetch_page(url, max_retries=3):
    """
    Fetch một trang HTML với headers ngẫu nhiên và retry khi bị chặn (429).
    """
    for attempt in range(max_retries):
        try:
            headers = get_headers()
            response = requests.get(url, headers=headers, timeout=15)

            if response.status_code == 429:  # bị rate limit
                wait_time = random.uniform(5, 10)
                logger.warning(f"Rate limited (429). Sleeping {wait_time:.1f}s...")
                time.sleep(wait_time)
                continue  # thử lại

            response.raise_for_status()

            # Thêm delay ngẫu nhiên để giả lập user thật
            sleep_time = random.uniform(2, 5)
            logger.debug(f"Sleeping {sleep_time:.1f}s before next request...")
            time.sleep(sleep_time)

            return BeautifulSoup(response.text, "html.parser")

        except Exception as e:
            logger.warning(f"Error fetching {url}: {e} (attempt {attempt+1})")
            time.sleep(random.uniform(3, 6))

    logger.error(f"Failed to fetch {url} after {max_retries} retries.")
    return None

def parse_job(card) -> dict:
    """
    Get the link to that job-card
    """
    h3_tag = card.find("h3", class_ = "title")
    if h3_tag:
        a_tag = h3_tag.find("a")
        if a_tag and a_tag.has_attr("href"):
            return {'title': a_tag.get_text(strip= True),'link':a_tag['href']}
    return None


def extract_jobs_from_page(html : str)-> list:
    """
    Get all links of jobs from that page 
    """
    cards = html.find_all("div", class_ = 'job-item-search-result')
    return [parse_job(card) for card in cards if parse_job(card)]

#====================================================================================================
def get_title_information(html,info_type):
    """
    Get the 'salary' or 'location' or 'experience'
    """
    patterns = {
        "salary": r"(mức lương|thu nhập)",
        "location": r"(địa điểm)",
        "experience": r"(kinh nghiệm)",
    }
    sections = html.find_all('div', class_ = 'job-detail__info--section-content')
    if sections:
        for section in sections:
            title = section.find('div',class_ = 'job-detail__info--section-content-title')
            if title:
                text = title.get_text(strip = True)
                if re.search(patterns[info_type],text,flags = re.IGNORECASE):
                    value = section.find('div', class_ = 'job-detail__info--section-content-value')
                    return value.get_text(strip = True) if value else None
    return None

def get_detail_information(html,info_type):
    """"""
    patterns = {
        'description':'mô tả công việc',
        'requirement':'yêu cầu ứng viên'
    }
    sections = html.find_all('div',class_ = 'job-description__item')
    if sections:
        for section in sections:
            title = section.find('h3')
            if title:
                text = title.get_text(strip = True)
                if re.search(patterns[info_type],text,flags=re.IGNORECASE):
                    value = section.find('div', class_ = 'job-description__item--content')
                    return value.get_text(strip = True) if value else None
    return None

def get_general_information(html,info_type):
    """
    Get 'position' or 'education' or 'quantity'
    """
    patterns = {
        'position': r'cấp bậc',
        'education':r'học vấn',
        'quantity': r'số lượng tuyển'
    }
    sections = html.find_all('div',class_ = 'box-general-group-info')
    if sections:
        for section in sections:
            title = section.find('div',class_ = 'box-general-group-info-title')
            if title:
                text = title.get_text(strip = True)
                if re.search(patterns[info_type],text, flags= re.IGNORECASE):
                    value = section.find('div',class_ = 'box-general-group-info-value')
                    return value.get_text(strip = True) if value else None
    return None
def get_company(html):
    tag = html.find('div',class_ = 'company-name-label')
    if tag:
        return tag.get_text(strip = True)
    return None
#===================================================================================================               


def fetch_job_detail(html):
    return {
        'description': get_detail_information(html,'description'),
        'requirement': get_detail_information(html,'requirement'),
        'location': get_title_information(html,'location'),
        'position': get_general_information(html,'position'),
        'education': get_general_information(html,'education'),
        'quantity' : get_general_information(html,'quantity'),
        'salary': get_title_information(html,'salary'),
        'experience': get_title_information(html,'experience'),
        'company': get_company(html)
    }


def extract_jobcv(n: int) -> list:
    """
    Crawl N job(s) from TobCV (multi-page)
    """
    page  = 1 
    base_url = "https://www.topcv.vn/tim-viec-lam-cong-nghe-thong-tin-cr257"
    jobs = []
    logger.info(f"Start extracting {n} jobs from TobCV")
    try:
        while len(jobs) < n and page < 72:
            url = f"{base_url}?page={page}"
            html = fetch_page(url)
            page_jobs = extract_jobs_from_page(html)
            for job in page_jobs:
                try:
                    logger.info(f"Crawling job: {job['title']}")
                    job_html = fetch_page(job['link'])
                    detail = fetch_job_detail(job_html)
                    
                    # merge job title, link and detail
                    job.update(detail)
                    jobs.append(job)

                    if len(jobs) >= n:
                        break
                except Exception as e:
                    logger.warning(f"Failed to fetch job {job['title']}: {e}")
            page +=1
            logger.info(f"Fetched successfully {len(jobs)} in page {page} so far...")
        logger.info(f"=========== Fetched successfully {n} jobs ==============")
    except Exception as e:
        logger.error(f"Error extracting jobCV {e}", exc_info = True)
    return jobs

if __name__ == '__main__':
    print(extract_jobcv(5))
        