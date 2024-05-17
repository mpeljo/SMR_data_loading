# Constants
NULL_VALUE = -99999
MAX_DEPTH = 100

# STAGE is "test" or "final"
STAGE = "final"

# Set translation from bayesian percentiles to database terminology,
#   where "lmh" means low-median-high
lmh = {
    "p5": "BAYESIAN_LOW",
    "p50": "BAYESIAN_MEDIAN",
    "p95": "BAYESIAN_HIGH",
}


# Locate template and input data config
full_template_file = (
    r".\Templates\Measure_Section-Samples-downhole intervals-rockprops_2023.10.XLSX"
)
smr_water_data_path = r"\\prod.lan\active\proj\futurex\DCD\Data\Processed\Geophysics\SMR\results\SMR_data_for_registration-8April2024.csv"
config_file = r".\Config\SMR_May2024_load_config_reprocessed.xlsx"

# Output files
test_output_file = "Test_ROCKPROPS_UDF_SMR_loader_May2024.XLSX"
final_output_file = "ROCKPROPS_reloader_UDF_SMR_acquired_2022-2023.XLSX"
output_dir = r".\Outputs\\"


# SECTION INTERVAL COLLECTION tab
COLLECTION_NAME_POSTFIX = " water content profile"
COLLECTION_TYPE = "hydrogeological"
ORIGINATOR_NUMBER = 484  # K.P. Tan
PREFERRED_COLLECTION = "Y"

# SECTION INTERVALS tab
INTERVAL_UNIT_OF_MEASURE = "metre"

# SAMPLES tab
ANO = 228  # Generic GA ANO
ACCESS_CODE = "A"  # Set to "GA-only" until director approvals
QA_STATUS = "C"
ACTIVITY_CODE = "A"
SAMPLE_TYPE = "observation only"
SAMPLING_METHOD = "field mapping survey"
MATERIAL_CLASS = "groundwater"
PROJECT_NO = 576

# SCALAR PROPERTIES (SP) tab
# ACCESS_CODE = "A"     # already defined via SAMPLES tab
SP_QA_STATUS = "U"
ORIGNO = 484  # K.P. Tan
SOURCE_TYPE = "GA NAS"
SOURCE = r"\\prod.lan\active\proj\futurex\DCD\Data\Processed\Geophysics\SMR\results"
LOAD_APPROVED = "Y"
PROCESS_TYPE = (
    17475995  # "Determination of total water content with Surface NMR apparatus"
)
PETROPHYSICAL_PROPERTY = "water content"
UOM = "volume fraction"
NUMERICAL_CONFIDENCE = "moderate confidence"
METADATA_QUALITY = "high quality"
SUMMARY_CONFIDENCE = "high confidence"
BAYESIAN_CONSTANTS = {
    "BAYESIAN_LOW": {
        "RESULT QUALIFIER": "Bayesian low",
        "UNCERTAINTY TYPE": "Bayesian posterior inferred percentile point",
        "UNCERTAINTY VALUE": 5,
        "UNCERTAINTY UOM": "percent",
        "SP_REMARKS": "Water content and uncertainty inferred from inverting SMR data using Bayesian probabilistic methods. The credible interval (u) is 90%, where u = high - low.",
    },
    "BAYESIAN_MEDIAN": {
        "RESULT QUALIFIER": "Bayesian median",
        "UNCERTAINTY TYPE": "Bayesian posterior inferred percentile point",
        "UNCERTAINTY VALUE": 50,
        "UNCERTAINTY UOM": "percent",
        "SP_REMARKS": "Water content and uncertainty inferred from inverting SMR data using Bayesian probabilistic methods.",
    },
    "BAYESIAN_HIGH": {
        "RESULT QUALIFIER": "Bayesian high",
        "UNCERTAINTY TYPE": "Bayesian posterior inferred percentile point",
        "UNCERTAINTY VALUE": 95,
        "UNCERTAINTY UOM": "percent",
        "SP_REMARKS": "Water content and uncertainty inferred from inverting SMR data using Bayesian probabilistic methods. The credible interval (u) is 90%, where u = high - low.",
    },
}
