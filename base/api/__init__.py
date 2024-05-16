import json
from base.api.url import *
from base.api.request import Request
from base.datasource import _redis
from base.api.data_to_class import json_to_class
from base.enums import config_enums, scope_id_enums
from base.entity.config import Config
from base.api.data_to_class import json_to_class
from base.entity.pro_file import ProFile
from base.entity.ads_info import AdsInfo


def get_profile():
    pro_file_list = Request.get(profile)
    return [json_to_class(i, ProFile) for i in pro_file_list]


def init(config_file_path: str) -> None:
    with open(config_file_path, "r") as f:
        _ = f.read()
    config = json_to_class(json.loads(_), Config)
    _redis.put_key(config_enums, config.to_dict())
    pro_file_list = get_profile()
    for i in pro_file_list:
        if i.countryCode == config.scope_code:
            _redis.put_key(scope_id_enums, i.profileId)


def get_ads_list():
    ads_list = Request.post(adsList, headers={
        "Accept": "application/vnd.spCampaign.v3+json",
        "Content-Type": "application/vnd.spCampaign.v3+json"
        })
    return [json_to_class(i, AdsInfo) for i in ads_list["campaigns"] if i["state"] == "ENABLED"]


def get_report_info(report_id: str):
    return Request.get(f"{reportList}{report_id}", headers={
        "Content-Type": "application/vnd.createasyncreportrequest.v3+json"
        })


def download_file(file_url: str):
    return Request.download(file_url)
