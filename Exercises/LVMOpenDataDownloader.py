# -*- coding: utf-8 -*-
'''
    Helper object for downloading LVMs Open data
'''
lvm_opendata_download_url = 'https://lvmgeo.lvm.lv/PublicData/'

import urllib, urlparse
uj = urlparse.urljoin

def LVM_APGRIESANAS_LAUKUMI (download_to_filename, format = 'GDB'):
    if format.upper() == 'GDB':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'GDB/'), 'LVM_APGRIESANAS_LAUKUMI.zip'), download_to_filename)
    if format.upper() == 'SHP':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'SHP/'), 'LVM_APGRIESANAS_LAUKUMI.zip'), download_to_filename)

def LVM_ATJAUNOJAMIE_MELIORACIJAS_OBJEKTI (download_to_filename, format = 'GDB'):
    if format.upper() == 'GDB':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'GDB/'), 'LVM_ATJAUNOJAMIE_MELIORACIJAS_OBJEKTI.zip'), download_to_filename)
    if format.upper() == 'SHP':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'SHP/'), 'LVM_ATJAUNOJAMIE_MELIORACIJAS_OBJEKTI.zip'), download_to_filename)

def LVM_ATTISTAMIE_AUTOCELI (download_to_filename, format = 'GDB'):
    if format.upper() == 'GDB':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'GDB/'), 'LVM_ATTISTAMIE_AUTOCELI.zip'), download_to_filename)
    if format.upper() == 'SHP':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'SHP/'), 'LVM_ATTISTAMIE_AUTOCELI.zip'), download_to_filename)

def LVM_AUTOCELU_APRIKOJUMS (download_to_filename, format = 'GDB'):
    if format.upper() == 'GDB':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'GDB/'), 'LVM_AUTOCELU_APRIKOJUMS.zip'), download_to_filename)
    if format.upper() == 'SHP':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'SHP/'), 'LVM_AUTOCELU_APRIKOJUMS.zip'), download_to_filename)

def LVM_BOJAJUMU_RISKS_2018 (download_to_filename, format = 'GDB'):
    if format.upper() == 'GDB':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'GDB/'), 'LVM_BOJAJUMU_RISKS_2018.zip'), download_to_filename)
    if format.upper() == 'SHP':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'SHP/'), 'LVM_BOJAJUMU_RISKS_2018.zip'), download_to_filename)

def LVM_CAURTEKAS (download_to_filename, format = 'GDB'):
    if format.upper() == 'GDB':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'GDB/'), 'LVM_CAURTEKAS.zip'), download_to_filename)
    if format.upper() == 'SHP':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'SHP/'), 'LVM_CAURTEKAS.zip'), download_to_filename)

def LVM_EKOMEZI (download_to_filename, format = 'GDB'):
    if format.upper() == 'GDB':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'GDB/'), 'LVM_EKOMEZI.zip'), download_to_filename)
    if format.upper() == 'SHP':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'SHP/'), 'LVM_EKOMEZI.zip'), download_to_filename)

def LVM_GRAVJI (download_to_filename, format = 'GDB'):
    if format.upper() == 'GDB':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'GDB/'), 'LVM_GRAVJI.zip'), download_to_filename)
    if format.upper() == 'SHP':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'SHP/'), 'LVM_GRAVJI.zip'), download_to_filename)

def LVM_IECIRKNI (download_to_filename, format = 'GDB'):
    if format.upper() == 'GDB':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'GDB/'), 'LVM_IECIRKNI.zip'), download_to_filename)
    if format.upper() == 'SHP':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'SHP/'), 'LVM_IECIRKNI.zip'), download_to_filename)

def LVM_IZMAINISANAS_VIETAS (download_to_filename, format = 'GDB'):
    if format.upper() == 'GDB':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'GDB/'), 'LVM_IZMAINISANAS_VIETAS.zip'), download_to_filename)
    if format.upper() == 'SHP':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'SHP/'), 'LVM_IZMAINISANAS_VIETAS.zip'), download_to_filename)

def LVM_KVARTALI (download_to_filename, format = 'GDB'):
    if format.upper() == 'GDB':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'GDB/'), 'LVM_KVARTALI.zip'), download_to_filename)
    if format.upper() == 'SHP':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'SHP/'), 'LVM_KVARTALI.zip'), download_to_filename)

def LVM_MEZA_AUTOCELI (download_to_filename, format = 'GDB'):
    if format.upper() == 'GDB':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'GDB/'), 'LVM_MEZA_AUTOCELI.zip'), download_to_filename)
    if format.upper() == 'SHP':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'SHP/'), 'LVM_MEZA_AUTOCELI.zip'), download_to_filename)

def LVM_MEZA_MELIORACIJAS_SISTEMAS (download_to_filename, format = 'GDB'):
    if format.upper() == 'GDB':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'GDB/'), 'LVM_MEZA_MELIORACIJAS_SISTEMAS.zip'), download_to_filename)
    if format.upper() == 'SHP':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'SHP/'), 'LVM_MEZA_MELIORACIJAS_SISTEMAS.zip'), download_to_filename)

def LVM_MINERALIZETAS_JOSLAS (download_to_filename, format = 'GDB'):
    if format.upper() == 'GDB':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'GDB/'), 'LVM_MINERALIZETAS_JOSLAS.zip'), download_to_filename)
    if format.upper() == 'SHP':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'SHP/'), 'LVM_MINERALIZETAS_JOSLAS.zip'), download_to_filename)

def LVM_NOBRAUKTUVES (download_to_filename, format = 'GDB'):
    if format.upper() == 'GDB':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'GDB/'), 'LVM_NOBRAUKTUVES.zip'), download_to_filename)
    if format.upper() == 'SHP':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'SHP/'), 'LVM_NOBRAUKTUVES.zip'), download_to_filename)

def LVM_NOGABALI (download_to_filename, format = 'GDB'):
    if format.upper() == 'GDB':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'GDB/'), 'LVM_NOGABALI.zip'), download_to_filename)
    if format.upper() == 'SHP':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'SHP/'), 'LVM_NOGABALI.zip'), download_to_filename)

def LVM_REGIONI (download_to_filename, format = 'GDB'):
    if format.upper() == 'GDB':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'GDB/'), 'LVM_REGIONI.zip'), download_to_filename)
    if format.upper() == 'SHP':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'SHP/'), 'LVM_REGIONI.zip'), download_to_filename)

def LVM_SABIEDRIBAI_NOZIMIGAS_VIETAS (download_to_filename, format = 'GDB'):
    if format.upper() == 'GDB':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'GDB/'), 'LVM_SABIEDRIBAI_NOZIMIGAS_VIETAS.zip'), download_to_filename)
    if format.upper() == 'SHP':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'SHP/'), 'LVM_SABIEDRIBAI_NOZIMIGAS_VIETAS.zip'), download_to_filename)

def LVM_STIGAS (download_to_filename, format = 'GDB'):
    if format.upper() == 'GDB':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'GDB/'), 'LVM_STIGAS.zip'), download_to_filename)
    if format.upper() == 'SHP':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'SHP/'), 'LVM_STIGAS.zip'), download_to_filename)

def LVM_TILTI_CAURTEKAS (download_to_filename, format = 'GDB'):
    if format.upper() == 'GDB':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'GDB/'), 'LVM_TILTI_CAURTEKAS.zip'), download_to_filename)
    if format.upper() == 'SHP':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'SHP/'), 'LVM_TILTI_CAURTEKAS.zip'), download_to_filename)

def LVM_UDENS_NEMSANAS_V (download_to_filename, format = 'GDB'):
    if format.upper() == 'GDB':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'GDB/'), 'LVM_UDENS_NEMSANAS_V.zip'), download_to_filename)
    if format.upper() == 'SHP':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'SHP/'), 'LVM_UDENS_NEMSANAS_V.zip'), download_to_filename)

def LVM_UGUNSGREKI_TER (download_to_filename, format = 'GDB'):
    if format.upper() == 'GDB':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'GDB/'), 'LVM_UGUNSGREKI_TER.zip'), download_to_filename)
    if format.upper() == 'SHP':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'SHP/'), 'LVM_UGUNSGREKI_TER.zip'), download_to_filename)

def LVM_UGUNSGREKI_VIETAS (download_to_filename, format = 'GDB'):
    if format.upper() == 'GDB':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'GDB/'), 'LVM_UGUNSGREKI_VIETAS.zip'), download_to_filename)
    if format.upper() == 'SHP':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'SHP/'), 'LVM_UGUNSGREKI_VIETAS.zip'), download_to_filename)

def LVM_ZEMES_VIENIBAS (download_to_filename, format = 'GDB'):
    if format.upper() == 'GDB':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'GDB/'), 'LVM_ZEMES_VIENIBAS.zip'), download_to_filename)
    if format.upper() == 'SHP':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'SHP/'), 'LVM_ZEMES_VIENIBAS.zip'), download_to_filename)

def MEZA_PETISANAS_STACIJA_KVARTALI (download_to_filename, format = 'GDB'):
    if format.upper() == 'GDB':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'GDB/'), 'MEZA_PETISANAS_STACIJA_KVARTALI.zip'), download_to_filename)
    if format.upper() == 'SHP':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'SHP/'), 'MEZA_PETISANAS_STACIJA_KVARTALI.zip'), download_to_filename)

def MEZA_PETISANAS_STACIJA_NOGABALI (download_to_filename, format = 'GDB'):
    if format.upper() == 'GDB':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'GDB/'), 'MEZA_PETISANAS_STACIJA_NOGABALI.zip'), download_to_filename)
    if format.upper() == 'SHP':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'SHP/'), 'MEZA_PETISANAS_STACIJA_NOGABALI.zip'), download_to_filename)

def MOFO_MEZA_IPASUMI_KVARTALI (download_to_filename, format = 'GDB'):
    if format.upper() == 'GDB':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'GDB/'), 'MOFO_MEZA_IPASUMI_KVARTALI.zip'), download_to_filename)
    if format.upper() == 'SHP':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'SHP/'), 'MOFO_MEZA_IPASUMI_KVARTALI.zip'), download_to_filename)

def MOFO_MEZA_IPASUMI_NOGABALI (download_to_filename, format = 'GDB'):
    if format.upper() == 'GDB':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'GDB/'), 'MOFO_MEZA_IPASUMI_NOGABALI.zip'), download_to_filename)
    if format.upper() == 'SHP':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'SHP/'), 'MOFO_MEZA_IPASUMI_NOGABALI.zip'), download_to_filename)

def SIA_BERGVIK_SKOG_KVARTALI (download_to_filename, format = 'GDB'):
    if format.upper() == 'GDB':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'GDB/'), 'SIA_BERGVIK_SKOG_KVARTALI.zip'), download_to_filename)
    if format.upper() == 'SHP':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'SHP/'), 'SIA_BERGVIK_SKOG_KVARTALI.zip'), download_to_filename)

def SIA_BERGVIK_SKOG_NOGABALI (download_to_filename, format = 'GDB'):
    if format.upper() == 'GDB':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'GDB/'), 'SIA_BERGVIK_SKOG_NOGABALI.zip'), download_to_filename)
    if format.upper() == 'SHP':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'SHP/'), 'SIA_BERGVIK_SKOG_NOGABALI.zip'), download_to_filename)

def SIA_BERGVIK_SKOG_ZEMES_VIENIBAS (download_to_filename, format = 'GDB'):
    if format.upper() == 'GDB':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'GDB/'), 'SIA_BERGVIK_SKOG_ZEMES_VIENIBAS.zip'), download_to_filename)
    if format.upper() == 'SHP':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'SHP/'), 'SIA_BERGVIK_SKOG_ZEMES_VIENIBAS.zip'), download_to_filename)

def SIA_KURSA_MRU_KVARTALI (download_to_filename, format = 'GDB'):
    if format.upper() == 'GDB':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'GDB/'), 'SIA_KURSA_MRU_KVARTALI.zip'), download_to_filename)
    if format.upper() == 'SHP':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'SHP/'), 'SIA_KURSA_MRU_KVARTALI.zip'), download_to_filename)

def SIA_KURSA_MRU_NOGABALI (download_to_filename, format = 'GDB'):
    if format.upper() == 'GDB':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'GDB/'), 'SIA_KURSA_MRU_NOGABALI.zip'), download_to_filename)
    if format.upper() == 'SHP':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'SHP/'), 'SIA_KURSA_MRU_NOGABALI.zip'), download_to_filename)

def SIA_LATVIJAS_FINIERIS_MEZS_KVARTALI (download_to_filename, format = 'GDB'):
    if format.upper() == 'GDB':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'GDB/'), 'SIA_LATVIJAS_FINIERIS_MEZS_KVARTALI.zip'), download_to_filename)
    if format.upper() == 'SHP':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'SHP/'), 'SIA_LATVIJAS_FINIERIS_MEZS_KVARTALI.zip'), download_to_filename)

def SIA_LATVIJAS_FINIERIS_MEZS_NOGABALI (download_to_filename, format = 'GDB'):
    if format.upper() == 'GDB':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'GDB/'), 'SIA_LATVIJAS_FINIERIS_MEZS_NOGABALI.zip'), download_to_filename)
    if format.upper() == 'SHP':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'SHP/'), 'SIA_LATVIJAS_FINIERIS_MEZS_NOGABALI.zip'), download_to_filename)

def SIA_LATVIJAS_FINIERIS_MEZS_ZEMES_VIENIBAS (download_to_filename, format = 'GDB'):
    if format.upper() == 'GDB':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'GDB/'), 'SIA_LATVIJAS_FINIERIS_MEZS_ZEMES_VIENIBAS.zip'), download_to_filename)
    if format.upper() == 'SHP':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'SHP/'), 'SIA_LATVIJAS_FINIERIS_MEZS_ZEMES_VIENIBAS.zip'), download_to_filename)

def SIA_MANA_MEZS_KVARTALI (download_to_filename, format = 'GDB'):
    if format.upper() == 'GDB':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'GDB/'), 'SIA_MANA_MEZS_KVARTALI.zip'), download_to_filename)
    if format.upper() == 'SHP':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'SHP/'), 'SIA_MANA_MEZS_KVARTALI.zip'), download_to_filename)

def SIA_MANA_MEZS_NOGABALI (download_to_filename, format = 'GDB'):
    if format.upper() == 'GDB':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'GDB/'), 'SIA_MANA_MEZS_NOGABALI.zip'), download_to_filename)
    if format.upper() == 'SHP':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'SHP/'), 'SIA_MANA_MEZS_NOGABALI.zip'), download_to_filename)

def SIA_ROSTERS_KVARTALI (download_to_filename, format = 'GDB'):
    if format.upper() == 'GDB':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'GDB/'), 'SIA_ROSTERS_KVARTALI.zip'), download_to_filename)
    if format.upper() == 'SHP':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'SHP/'), 'SIA_ROSTERS_KVARTALI.zip'), download_to_filename)

def SIA_ROSTERS_NOGABALI (download_to_filename, format = 'GDB'):
    if format.upper() == 'GDB':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'GDB/'), 'SIA_ROSTERS_NOGABALI.zip'), download_to_filename)
    if format.upper() == 'SHP':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'SHP/'), 'SIA_ROSTERS_NOGABALI.zip'), download_to_filename)

def SIA_SUNDIN_KVARTALI (download_to_filename, format = 'GDB'):
    if format.upper() == 'GDB':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'GDB/'), 'SIA_SUNDIN_KVARTALI.zip'), download_to_filename)
    if format.upper() == 'SHP':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'SHP/'), 'SIA_SUNDIN_KVARTALI.zip'), download_to_filename)

def SIA_SUNDIN_NOGABALI (download_to_filename, format = 'GDB'):
    if format.upper() == 'GDB':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'GDB/'), 'SIA_SUNDIN_NOGABALI.zip'), download_to_filename)
    if format.upper() == 'SHP':
        urllib.urlretrieve(uj(uj(lvm_opendata_download_url, 'SHP/'), 'SIA_SUNDIN_NOGABALI.zip'), download_to_filename)

