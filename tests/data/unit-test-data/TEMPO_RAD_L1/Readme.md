## 3 CSV files created for TEMPO_RAD_L1_V04_20260425T205950Z_S011G09_subsetted.nc based on dimensional schemas


### TEMPO_RAD_L1_V04_20260425T205950Z_S011G09_subsetted.nc-0_reformatted.csv
	dimensions:   mirror_step
	non-dimension coordinates:
	1 variables:
		/time

### TEMPO_RAD_L1_V04_20260425T205950Z_S011G09_subsetted.nc-1_reformatted.csv
	dimensions:   mirror_step, xtrack
	non-dimension coordinates:
	6 variables:
		/band_290_490_nm/latitude
		/band_290_490_nm/longitude
		/band_290_490_nm/solar_azimuth_angle
		/band_540_740_nm/latitude
		/band_540_740_nm/longitude
		/band_540_740_nm/solar_azimuth_angle

### TEMPO_RAD_L1_V04_20260425T205950Z_S011G09_subsetted.nc-2_reformatted.csv
	dimensions:   mirror_step, xtrack, corner
	non-dimension coordinates:
	4 variables:
		/band_290_490_nm/latitude_bounds
		/band_290_490_nm/longitude_bounds
		/band_540_740_nm/latitude_bounds
		/band_540_740_nm/longitude_bounds


# TEMPO_RAD_L1_V04_20260425T205950Z_S011G09_subsetted.nc Global Attributes:
		Conventions: CF-1.6, ACDD-1.3
		begin_date: 2026-04-25
		begin_time: 20:59:50
		collection_shortname: TEMPO_RAD_L1
		collection_version: 1
		coremetadata: GROUP                  = INVENTORYMETADATA
		GROUPTYPE            = MASTERGROUP
		GROUP                  = ECSDATAGRANULE
		OBJECT                 = LOCALGRANULEID
		NUM_VAL              = 1
		VALUE                = "TEMPO_RAD_L1_V04_20260425T205950Z_S011G09.nc"
		END_OBJECT             = LOCALGRANULEID
		OBJECT                 = LOCALVERSIONID
		NUM_VAL              = 1
		VALUE                = ("RFC1321 MD5 = not yet calculated")
		END_OBJECT             = LOCALVERSIONID
		OBJECT                 = PRODUCTIONDATETIME
		NUM_VAL              = 1
		VALUE                = "2026-04-25T21:32:06Z"
		END_OBJECT             = PRODUCTIONDATETIME
		END_GROUP              = ECSDATAGRANULE
		GROUP                  = COLLECTIONDESCRIPTIONCLASS
		OBJECT                 = SHORTNAME
		NUM_VAL              = 1
		VALUE                = "TEMPO_RAD_L1"
		END_OBJECT             = SHORTNAME
		OBJECT                 = VERSIONID
		NUM_VAL              = 1
		VALUE                = 4
		END_OBJECT             = VERSIONID
		END_GROUP              = COLLECTIONDESCRIPTIONCLASS
		GROUP                  = INPUTGRANULE
		OBJECT                 = INPUTPOINTER
		NUM_VAL              = 14
		VALUE                = ("TEMPO_RAD_L0_V01_20260425T205950Z_S011G09.nc", "TEMPO_HK_L0_V01_20260425T205206Z.nc", "TEMPO_HK_L0_V01_20260425T205642Z.nc", "TEMPO_HK_L0_V01_20260425T210106Z.nc", "TEMPO_HK_L0_V01_20260425T210546Z.nc", "TEMPO_HK_L0_V01_20260425T211007Z.nc", "TEMPO_IRR_L1_V04_20260423T040511Z.nc", "TEMPO_DRK_L1_V04_20260425T110315Z.nc", "TEMPO_SMC_L0_V01_20260425T205635Z.nc", "TEMPO_SMC_L0_V01_20260425T210134Z.nc", "TEMPO_SMC_L0_V01_20260425T210534Z.nc", "TEMPO_IRU_L0_V01_20260425T205628Z.nc", "TEMPO_IRU_L0_V01_20260425T210028Z.nc", "TEMPO_IRU_L0_V01_20260425T210428Z.nc")
		END_OBJECT             = INPUTPOINTER
		END_GROUP              = INPUTGRANULE
		GROUP                  = SPATIALDOMAINCONTAINER
		GROUP                  = HORIZONTALSPATIALDOMAINCONTAINER
		GROUP                  = GPOLYGON
		OBJECT                 = GPOLYGONCONTAINER
		CLASS                = "1"
		GROUP                  = GRINGPOINT
		CLASS                = "1"
		OBJECT                 = GRINGPOINTLONGITUDE
		NUM_VAL              = 160
		CLASS                = "1"
		VALUE                = (-142.6531, -142.7654, -142.6443, -142.9761, -142.8548, -143.0777, -142.9568, -143.1795, -143.0589, -143.2836, -143.1634, -143.3889, -143.2689, -143.4952, -143.3755, -143.5986, -143.4792, -143.7127, -143.5934, -143.8182, -143.6992, -143.9302, -143.8114, -144.0382, -143.9197, -144.2665, -144.1482, -144.3861, -144.2678, -144.623, -144.5056, -144.7445, -144.628, -144.8704, -144.7539, -144.9921, -144.8756, -145.1161, -144.9996, -145.1212, -145.0053, -145.2484, -145.1386, -145.5126, -145.4063, -145.649, -145.5453, -145.7955, -145.6868, -145.9365, -145.8365, -146.0851, -145.9855, -146.237, -146.1374, -146.3913, -146.2782, -146.4054, -146.3074, -146.5641, -146.4686, -146.7247, -146.6125, -146.7397, -146.6419, -146.9034, -146.7918, -146.9223, -146.8275, -147.0908, -146.9797, -147.1119, -147.0159, -147.2804, -147.1698, -147.302, -147.1918, -147.3406, -147.2312, -147.4993, -147.3894, -147.5415, -147.4324, -147.5634, -147.4547, -147.7247, -147.6155, -147.7736, -147.6651, -147.8032, -147.695, -147.9619, -147.8533, -147.9905, -147.8821, -148.0179, -147.9356, -148.0755, -147.9942, -148.2685, -148.1608, -148.2996, -148.1922, -148.33, -148.2229, -148.3907, -148.315, -148.4549, -148.3488, -148.4868, -148.3809, -148.5199, -148.4142, -148.6942, -148.5879, -148.727, -148.6209, -148.7923, -148.6867, -148.8319, -148.7265, -148.8663, -148.794, -148.9709, -148.8664, -149.0098, -146.0957, -143.2957, -140.6644, -138.1443, -135.8157, -133.6305, -131.5902, -129.7295, -128.0437, -126.5023, -125.1074, -123.8568, -122.7522, -121.7802, -120.9409, -120.2319, -113.4238, -114.0504, -114.8186, -115.7306, -116.7893, -117.8911, -119.3297, -120.905, -122.5106, -124.4349, -126.4312, -128.6247, -131.0329, -133.5773, -136.3369, -139.2542, -142.4232, -142.6531)
		END_OBJECT             = GRINGPOINTLONGITUDE
		OBJECT                 = GRINGPOINTLATITUDE
		NUM_VAL              = 160
		CLASS                = "1"
		VALUE                = (59.12663, 59.10607, 59.05617, 58.99421, 58.94446, 58.90366, 58.85409, 58.81332, 58.76394, 58.72421, 58.67499, 58.63464, 58.58559, 58.54691, 58.49803, 58.45785, 58.40913, 58.37167, 58.3231, 58.2834, 58.235, 58.19718, 58.14892, 58.11018, 58.06207, 57.93994, 57.89211, 57.85589, 57.74223, 57.62254, 57.57526, 57.54029, 57.42779, 57.39336, 57.3465, 57.31152, 57.26476, 57.22987, 57.18323, 57.16644, 57.11995, 57.08535, 56.97571, 56.86311, 56.7546, 56.72051, 56.61374, 56.58199, 56.47331, 56.44178, 56.33584, 56.30374, 56.19922, 56.16733, 56.06289, 56.03223, 55.98753, 55.97221, 55.86787, 55.83832, 55.7344, 55.7054, 55.66119, 55.64613, 55.54224, 55.51425, 55.47034, 55.45623, 55.35362, 55.32584, 55.28221, 55.26847, 55.16634, 55.13938, 55.09602, 55.0824, 55.03915, 54.96774, 54.92473, 54.89846, 54.85547, 54.78545, 54.74268, 54.72906, 54.6864, 54.66023, 54.61758, 54.5491, 54.50665, 54.49431, 54.45197, 54.4256, 54.38327, 54.37152, 54.32928, 54.31661, 54.21938, 54.20798, 54.11145, 54.08636, 54.04451, 54.03295, 53.99119, 53.97932, 53.93764, 53.87186, 53.77663, 53.76547, 53.72414, 53.71211, 53.67088, 53.65902, 53.61786, 53.59539, 53.55422, 53.54251, 53.50142, 53.43698, 53.39606, 53.38575, 53.3449, 53.33358, 53.24014, 53.17717, 53.13663, 53.12589, 51.9017, 50.52023, 49.00489, 47.3176, 45.5105, 43.55012, 41.43489, 39.20685, 36.87824, 34.42004, 31.84456, 29.1606, 26.39043, 23.51897, 20.56217, 17.53159, 17.38955, 21.0542, 24.6285, 28.08882, 31.41924, 34.37292, 37.6152, 40.58718, 43.17314, 45.81979, 48.17509, 50.39304, 52.4752, 54.3548, 56.09446, 57.65908, 59.09768, 59.12663)
		END_OBJECT             = GRINGPOINTLATITUDE
		OBJECT                 = GRINGPOINTSEQUENCENO
		NUM_VAL              = 160
		CLASS                = "1"
		VALUE                = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160)
		END_OBJECT             = GRINGPOINTSEQUENCENO
		END_GROUP              = GRINGPOINT
		GROUP                  = GRING
		CLASS                = "1"
		OBJECT                 = EXCLUSIONGRINGFLAG
		NUM_VAL              = 1
		VALUE                = "N"
		CLASS                = "1"
		END_OBJECT             = EXCLUSIONGRINGFLAG
		END_GROUP              = GRING
		END_OBJECT             = GPOLYGONCONTAINER
		END_GROUP              = GPOLYGON
		END_GROUP              = HORIZONTALSPATIALDOMAINCONTAINER
		END_GROUP              = SPATIALDOMAINCONTAINER
		GROUP                  = RANGEDATETIME
		OBJECT                 = RANGEENDINGDATE
		NUM_VAL              = 1
		VALUE                = "2026-04-25"
		END_OBJECT             = RANGEENDINGDATE
		OBJECT                 = RANGEENDINGTIME
		NUM_VAL              = 1
		VALUE                = "21:06:27"
		END_OBJECT             = RANGEENDINGTIME
		OBJECT                 = RANGEBEGINNINGDATE
		NUM_VAL              = 1
		VALUE                = "2026-04-25"
		END_OBJECT             = RANGEBEGINNINGDATE
		OBJECT                 = RANGEBEGINNINGTIME
		NUM_VAL              = 1
		VALUE                = "20:59:50"
		END_OBJECT             = RANGEBEGINNINGTIME
		END_GROUP              = RANGEDATETIME
		GROUP                  = PGEVERSIONCLASS
		OBJECT                 = PGEVERSION
		NUM_VAL              = 1
		VALUE                = "0.1.0"
		END_OBJECT             = PGEVERSION
		END_GROUP              = PGEVERSIONCLASS
		END_GROUP              = INVENTORYMETADATA
		END
		creator_url: http://tempo.si.edu
		day_of_year: 115
		end_date: 2026-04-25
		end_time: 21:06:27
		format_version: 2
		geospatial_bounds: POLYGON((-143.05894 55.17278, -143.05894 55.17278, -143.96837 55.58442, -143.96837 55.58442, -143.05894 55.17278))
		geospatial_bounds_crs: EPSG:4326
		geospatial_lat_max: 55.58442
		geospatial_lat_min: 55.16746
		geospatial_lon_max: -143.04753
		geospatial_lon_min: -143.96837
		granule_num: 9
		history: 2026-04-25T21:32:18Z: /proj/sdpc_soft/install/gnu-rocky8/sdpc/v4p8p3/bin/L0_ccd -vv --Version 4 --config l0_ccd.cfg -i @hk.lis --solar /proj/sdpc_archive/temposdpc/ops5/L1/IRR/D16908/20260423T040511Z/TEMPO_IRR_L1_V04_20260423T040511Z.nc --trend trend_params.nc -d /proj/sdpc_archive/temposdpc/ops5/L1/DRK/D16911/20260425T110315Z/TEMPO_DRK_L1_V04_20260425T110315Z.nc -o TEMPO_RAD_L1_V04_20260425T205950Z_S011G09.nc TEMPO_RAD_L0_V01_20260425T205950Z_S011G09.nc
		2026-04-25T21:35:21Z: /proj/sdpc_soft/install/gnu-rocky8/sdpc/v4p8p3/bin/L1_inr_prep -v 1 -i /proj/sdpc_archive/ancillary/var/iers/files/bulletina_2026106_xxxix_016.txt TEMPO_RAD_L1_V04_20260425T205950Z_S011G09.nc
		2026-04-25T21:47:24Z: /proj/sdpc_soft/install/gnu-rocky8/sdpc/v4p8p3/bin/L1_inr_post -vv -c /proj/sdpc/liveroot/temposdpc/ops5/etc/l1_inr_post.cfg -s /proj/sdpc_archive/ancillary/var/ims/2026/ims2026115_1km_v1.3.nc TEMPO_RAD_L1_V04_20260425T205950Z_S011G09.nc
		2026-04-25T23:10:17Z: /proj/sdpc_soft/install/gnu-rocky8/sdpc/v4p8p3/bin/wavecal_merge --delete -t TEMPO_RAD_L1_V04_20260425T205950Z_S011G09.nc wavecal_TEMPO_RAD_L1_V04_20260425T205950Z_S011G09
		2026-11-18 19:41:09.493070 podaac-l2ss-py v3.4.0rc3 (cut=True, pixel_subset=False, bbox=[[-144, -143], [55, 56]], min_time=2026-04-25T21:03:15.000Z, max_time=2026-04-25T21:03:18.000Z, variables=['band_290_490_nm/solar_azimuth_angle', 'band_540_740_nm/solar_azimuth_angle'])
		history_json: [{"date_time": "2026-11-18T19:41:09.493102+00:00", "derived_from": "47cc08d30302f06489bfc586140b744ea87c008ed06b1ef2449a4c513be04516.nc", "program": "podaac-l2ss-py", "version": "3.4.0rc3", "parameters": {"cut": true, "pixel_subset": false, "bbox": [[-144, -143], [55, 56]], "min_time": "2026-04-25T21:03:15.000Z", "max_time": "2026-04-25T21:03:18.000Z", "variables": ["band_290_490_nm/solar_azimuth_angle", "band_540_740_nm/solar_azimuth_angle"]}, "program_ref": "https://cmr.earthdata.nasa.gov:443/search/concepts/S1962070864-POCLOUD", "$schema": "https://harmony.earthdata.nasa.gov/schemas/history/0.1.0/history-v0.1.0.json"}]
		input_files: ['TEMPO_RAD_L0_V01_20260425T205950Z_S011G09.nc', 'TEMPO_HK_L0_V01_20260425T205206Z.nc', 'TEMPO_HK_L0_V01_20260425T205642Z.nc', 'TEMPO_HK_L0_V01_20260425T210106Z.nc', 'TEMPO_HK_L0_V01_20260425T210546Z.nc', 'TEMPO_HK_L0_V01_20260425T211007Z.nc', 'TEMPO_IRR_L1_V04_20260423T040511Z.nc', 'TEMPO_DRK_L1_V04_20260425T110315Z.nc', 'TEMPO_SMC_L0_V01_20260425T205635Z.nc', 'TEMPO_SMC_L0_V01_20260425T210134Z.nc', 'TEMPO_SMC_L0_V01_20260425T210534Z.nc', 'TEMPO_IRU_L0_V01_20260425T205628Z.nc', 'TEMPO_IRU_L0_V01_20260425T210028Z.nc', 'TEMPO_IRU_L0_V01_20260425T210428Z.nc']
		inr_status: 2
		institution: Smithsonian Astrophysical Observatory
		keywords: EARTH SCIENCE>ATMOSPHERE>ATMOSPHERIC RADIATION>RADIATIVE FLUX
		local_granule_id: TEMPO_RAD_L1_V04_20260425T205950Z_S011G09.nc
		pge_version: 0.1.0
		platform: Intelsat 40e
		processing_level: 1
		processing_version: 4
		product_type: RAD
		production_date_time: 2026-04-25T21:32:06Z
		project: TEMPO
		scan_num: 11
		scan_type: 0
		sdpc_version: TEMPO_SDPC_v4.8.3
		shortname: TEMPO_RAD_L1
		source: UV-VIS hyperspectral imaging
		summary: Level 1 radiance files provide radiance information at TEMPO’s native spatial resolution, ~10 km^2 at the center of the Field of Regard (FOR), for individual granules. Each granule covers the entire North-South TEMPO FOR but only a portion of the East-West FOR. The files are provided in netCDF4 format, and contain information on radiometrically and wavelength calibrated and geolocated radiances for the UV and visible bands, corresponding noise, parameterized wavelength grid, geolocation, viewing geometry, quality flags and other ancillary information. The product is produced using the L0-1b processor which includes multiple steps: (1) Image processing to produce radiometrically calibrated radiance, (2) Additional wavelength calibration to improve wavelength registration, (3) Image Navigation and Registration (INR) using GOES-R data, and (4) post INR processing geolocation tagging and polarization correction. Please refer to the ATBD for details.
		time_coverage_end: 2026-04-25T21:06:27Z
		time_coverage_end_since_epoch: 1461186405.6410873
		time_coverage_start: 2026-04-25T20:59:50Z
		time_coverage_start_since_epoch: 1461186008.7423465
		time_reference: 1980-01-06T00:00:00Z
		title: TEMPO Level 1 radiance measurement
		version_id: 4

# Group /band_290_490_nm Attributes:
		terrain_referenced_coordinates: yes
# Group /band_540_740_nm Attributes:
		terrain_referenced_coordinates: yes
# Group /inr_input/ephemeris Attributes:
		source: GPSR
