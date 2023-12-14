import logging
from dynaconf import Dynaconf, Validator, ValidationError

logger = logging.getLogger(__name__)

settings = Dynaconf(
    envvar_prefix=False,
    validators=[
        Validator("PORT", must_exist=True),
        Validator("DEBUG", must_exist=True),
    ],
)

try:
    settings.validators.validate_all()
except ValidationError as e:
    accumulative_errors = e.details
    logger.critical("FATAL ERROR: The following required settings are missing:")
    for error in accumulative_errors:
        logger.critical(f"{error[1]}")
    logger.critical("Exiting...")
    raise SystemExit(1)

settings.level = logging.DEBUG if settings.DEBUG else logging.INFO
