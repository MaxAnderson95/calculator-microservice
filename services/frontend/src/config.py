import logging
from dynaconf import validator, Dynaconf, Validator, ValidationError

logger = logging.getLogger(__name__)

settings = Dynaconf(
    envvar_prefix=False,
    validators=[
        Validator("ADD_SERVICE_URL", must_exist=True),
        Validator("SUBTRACT_SERVICE_URL", must_exist=True),
        Validator("MULTIPLY_SERVICE_URL", must_exist=True),
        Validator("DIVIDE_SERVICE_URL", must_exist=True),
        Validator("REDIS_HOST", default="localhost"),
        Validator("REDIS_PORT", default=6379),
        Validator("PORT", must_exist=True),
        Validator("DEBUG", default=False),
    ],
)


def check_database_config(settings: Dynaconf) -> None:
    db_vars = ['DB_HOST', 'DB_PORT', 'DB_USER', 'DB_PASSWORD', 'DB_NAME']
    set_vars = [var for var in db_vars if settings.get(var)]

    if set_vars and len(set_vars) != len(db_vars):
        raise ValidationError(
            "If any of DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME are set, all must be set."
        )

    if not set_vars and not settings.get('DB_URL'):
        logger.info("No database configuration detected. Using SQLite...")
        settings['DB_URL'] = "sqlite:///calculation_log.db"
    elif settings.get('DB_URL'):
        logger.info("Using database configuration from DB_URL...")
    else:
        logger.info("Using database configuration from environment variables...")


try:
    settings.validators.validate_all()
    check_database_config(settings)
except ValidationError as e:
    accumulative_errors = e.details
    logger.critical("FATAL ERROR: The following required settings are missing:")
    for error in accumulative_errors:
        logger.critical(f"{error[1]}")
    logger.critical("Exiting...")
    raise SystemExit(1)

settings.level = logging.DEBUG if settings.DEBUG else logging.INFO
