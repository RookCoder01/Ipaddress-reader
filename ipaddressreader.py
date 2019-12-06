import socket
            # Secure sites
list_dom = ['autodiscover.ombudsman.ky', 'autodiscover.gov.ky', 'awa.gov.ky', 'caymanaeoiportal.gov.ky', 'eas.gov.ky',
            'geo.caymanlandinfo.ky', 'investcayman.ky', 'legislation.gov.ky', 'my.caymanlandinfo.ky',
            'new.caymanlandinfo.ky', 'ombudsman.ky', 'uniregistry.com', 'cinico.ky', 'ciregistry.ky', 'dcs.gov.ky',
            'internalaudit.gov.ky', 'nwda.gov.ky', 'ofreg.ky', 'plancayman.ky', 'planning.ky', 'pspb.ky', 'rcips.ky',
            'registry.gov.ky', 'rs.gov.ky', 'schools.edu.ky', 'sps.gov.ky', 'tab.ky', 'test.gov.ky',
            'testadapter.caymanlandinfo.ky', 'testgeo.caymanlandinfo.ky', 'tracker.caymanlandinfo.ky', 'uonline.gov.ky',
            'verify.gov.ky', 'webmail.gov.ky', 'caymanaeoiportal.gov.ky', 'caymanairports.com', 'caymanairways.com',
            'caymanport.com', 'cicadetcorps.ky', 'cifilm.ky', 'cima.ky', 'cinico.ky', 'ciregistry.gov.ky',
            'ciregistry.ky', 'cishipping.com', 'cpi.gov.ky', 'csx.ky', 'eso.ky', 'internalaudit.gov.ky',
            'investcayman.ky', 'legislation.gov.ky', 'museum.ky', 'nwda.gov.ky', 'occ.gov.ky', 'ofreg.ky',
            'ombudsman.ky', 'plancayman.gov.ky', 'planning.gov.ky', 'pspb.ky', 'rcips.ky', 'registry.gov.ky',
            'test.gov.ky', 'turtle.ky', 'ucci.edu.ky', 'vehicleinspections.gov.ky', 'verify.gov.ky',
            'visitcaymanislands.com', 'waterauthority.ky', 'worc.gov.ky',
            # Insecure Sites
            '911.gov.ky', 'amlu.gov.ky', 'anticorruptioncommission.ky',
            'gov.ky', 'caa.gov.ky', 'caymanfinance.gov.ky', 'caymanlibraries.gov.ky', 'caymanpost.gov.ky', 'caymanprepared.gov.ky',
            'caymanspirit.gov.ky', 'aoa.ky', 'cabinetoffice.gov.ky', 'archive.caymanrecovery.gov.ky', 'auditorgeneral.gov.ky',
            'cbc.gov.ky', 'centraltenders.gov.ky', 'cifs.gov.ky', 'ciipo.ky', 'cila.ky', 'cina.gov.ky', 'cipl.gov.ky', 'civilserviceappealscommission.ky',
            'commissionssecretariat.gov.ky', 'constitution.gov.ky', 'constitutionalcommission.ky', 'civilserviceappealscommission.ky',
            'csc.gov.ky', 'csd.gov.ky', 'centraltenders.gov.ky', 'cbc.gov.ky', 'cpiministry.gov.ky', 'dcfs.gov.ky', 'dci.gov.ky',
            'dcr.gov.ky', 'deh.gov.ky', 'departmentofsports.com', 'der.gov.ky', 'dhrs.gov.ky', 'diamondjubilee.gov.ky', 'districtadmin.gov.ky',
            'ditc.gov.ky', 'dlp.gov.ky', 'doa.gov.ky', 'dpp.gov.ky', 'dvdl.gov.ky', 'dves.gov.ky', 'ebc.gov.ky', 'education.gov.ky', 'eservices.gov.ky',
            'foi.gov.ky', 'fra.gov.ky', 'fraud.gov.ky', 'gazettes.gov.ky', 'genderequality.gov.ky', 'gov.ky', 'heroes.gov.ky', 'humanrightscommission.ky',
            'immigration.gov.ky', 'investcayman.gov.ky', 'jobs.gov.ky', 'judicialandlegalservicescommission.ky', 'lawreformcommission.gov.ky',
            'legislativeassembly.ky', 'lrc.gov.ky', 'maci.gov.ky', 'mcays.gov.ky', 'ministryofhealth.gov.ky', 'mof.gov.ky',
            'mtd.gov.ky', 'nau.gov.ky', 'npo.gov.ky', 'odg.gov.ky', 'oes.gov.ky', 'oftel.gov.ky', 'eservices.gov.ky', 'otp.gov.ky',
            'mof.gov.ky', 'cpiministry.gov.ky', 'pocs.gov.ky', 'cabinetoffice.gov.ky', 'recruitment.gov.ky', 'sm.gov.ky',
            'weather.ky',
            # Parts of page are not secure
            'radiocayman.gov.ky', 'dcs.gov.ky', 'rpcu.gov.ky', 'sharefile.gov.ky', 'sriu.gov.ky', 'sso.gov.ky',
            'sunrise.gov.ky', 'thehub.gov.ky', 'tia.gov.ky', 'treasury.gov.ky', 'ueservices.gov.ky', 'usso.gov.ky', 'uwww.gov.ky', 
            'unhis.gov.ky', 'weather.gov.ky', 'webmail.caymanlibraries.gov.ky', 'worldclass.gov.ky', 'amlu.gov.ky', 'anticorruptioncommission.ky',
            'aoa.ky', 'apps.gov.ky', 'auditorgeneral.gov.ky',  'caa.gov.ky', 'cabinetoffice.gov.ky', 'caymanfinance.gov.ky', 'caymanlandinfo.ky',
            'caymanlibraries.gov.ky', 'caymanpost.gov.ky', 'caymanprepared.gov.ky', 'caymanprepared.ky', 'caymanrecovery.gov.ky', 'caymanroads.com',
            'caymanspirit.gov.ky', 'cays.org.ky', 'cbc.gov.ky', 'cidb.ky', 'cifs.gov.ky', 'ciipo.gov.ky', 'cila.ky', 'cina.gov.ky',
            'cipl.gov.ky', 'civilserviceappealscommission.ky', 'commissionssecretariat.gov.ky', 'constitution.gov.ky', 'constitutionalcommission.ky',
            'csac.gov.ky', 'csc.gov.ky', 'csd.gov.ky', 'customs.gov.ky', 'dapah.gov.ky', 'dawla.gov.ky', 'dcfs.gov.ky', 'dci.gov.ky',
            'dcr.gov.ky', 'dcs.gov.ky', 'deh.gov.ky', 'dhrs.gov.ky', 'districtadmin.gov.ky', 'ditc.gov.ky', 'dlp.gov.ky', 'doa.gov.ky',
            'doe.ky', 'dpp.gov.ky', 'dvdl.gov.ky', 'dves.gov.ky', 'ebc.gov.ky', 'education.gov.ky', 'esau.gov.ky', 'eservices.gov.ky',
            'foi.gov.ky', 'fra.gov.ky', 'fraud.gov.ky', 'frc.gov.ky', 'gazettes.gov.ky', 'genderequality.gov.ky', 'gis.gov.ky',
            'gov.ky', 'heroes.gov.ky', 'humanrightscommission.ky', 'immigration.gov.ky', 'immigrationlaw.gov.ky', 'investcayman.gov.ky',
            'judicial.ky', 'judicialandlegalservicescommission.ky', 'lawreformcommission.gov.ky', 'lawschool.gov.ky', 'legislativeassembly.ky',
            'lrc.gov.ky', 'mcays.gov.ky', 'ministryofhealth.gov.ky', 'mof.gov.ky', 'mrcu.ky', 'mtd.gov.ky', 'nau.gov.ky',
            'neoc.gov.ky', 'npo.gov.ky', 'odg.gov.ky', 'oes.gov.ky', 'oftel.gov.ky', 'otp.gov.ky', 'pfe.gov.ky', 'plahi.gov.ky',
            'pocs.gov.ky', 'protocol.gov.ky', 'protocoloffice.gov.ky', 'publicworks.gov.ky', 'radiocayman.gov.ky', 'recruitment.gov.ky',
            'rpcu.gov.ky', 'sriu.gov.ky', 'standardsinpubliclifecommission.ky', 'sunrise.gov.ky', 'tia.gov.ky', 'treasury.gov.ky',
            'weather.gov.ky', 'worldclass.gov.ky', 'wrc.gov.ky', 'ysu.gov.ky', 'pola.gov.ky', 'ysu.gov.ky']

for x in list_dom:
    print('IP of domain: ', x, socket.gethostbyname(x))
# Secure sites are finished
# Insecure sites are finished
# Parts of site are not secure finished
