import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import (
    CONF_CURRENT,
    DEVICE_CLASS_CURRENT,
    DEVICE_CLASS_EMPTY,
    DEVICE_CLASS_TEMPERATURE,
    DEVICE_CLASS_VOLTAGE,
    ICON_EMPTY,
    ICON_TIMELAPSE,
    STATE_CLASS_MEASUREMENT,
    UNIT_AMPERE,
    UNIT_CELSIUS,
    UNIT_EMPTY,
    UNIT_PERCENT,
    UNIT_VOLT,
)
from . import JkBms, CONF_JK_BMS_ID

DEPENDENCIES = ["jk_bms"]

CODEOWNERS = ["@syssi"]

CONF_CELL_VOLTAGE_1 = "cell_voltage_1"
CONF_CELL_VOLTAGE_2 = "cell_voltage_2"
CONF_CELL_VOLTAGE_3 = "cell_voltage_3"
CONF_CELL_VOLTAGE_4 = "cell_voltage_4"
CONF_CELL_VOLTAGE_5 = "cell_voltage_5"
CONF_CELL_VOLTAGE_6 = "cell_voltage_6"
CONF_CELL_VOLTAGE_7 = "cell_voltage_7"
CONF_CELL_VOLTAGE_8 = "cell_voltage_8"
CONF_CELL_VOLTAGE_9 = "cell_voltage_9"
CONF_CELL_VOLTAGE_10 = "cell_voltage_10"
CONF_CELL_VOLTAGE_11 = "cell_voltage_11"
CONF_CELL_VOLTAGE_12 = "cell_voltage_12"
CONF_CELL_VOLTAGE_13 = "cell_voltage_13"
CONF_CELL_VOLTAGE_14 = "cell_voltage_14"
CONF_CELL_VOLTAGE_15 = "cell_voltage_15"
CONF_CELL_VOLTAGE_16 = "cell_voltage_16"
CONF_CELL_VOLTAGE_17 = "cell_voltage_17"
CONF_CELL_VOLTAGE_18 = "cell_voltage_18"
CONF_CELL_VOLTAGE_19 = "cell_voltage_19"
CONF_CELL_VOLTAGE_20 = "cell_voltage_20"
CONF_CELL_VOLTAGE_21 = "cell_voltage_21"
CONF_CELL_VOLTAGE_22 = "cell_voltage_22"
CONF_CELL_VOLTAGE_23 = "cell_voltage_23"
CONF_CELL_VOLTAGE_24 = "cell_voltage_24"

CONF_POWER_TUBE_TEMPERATURE = "power_tube_temperature"
CONF_TEMPERATURE_SENSOR_1 = "temperature_sensor_1"
CONF_TEMPERATURE_SENSOR_2 = "temperature_sensor_2"
CONF_TOTAL_VOLTAGE = "total_voltage"
CONF_CAPACITY_REMAINING = "capacity_remaining"
CONF_TEMPERATURE_SENSORS = "temperature_sensors"
CONF_CHARGING_CYCLES = "charging_cycles"
CONF_TOTAL_CHARGING_CYCLE_CAPACITY = "total_charging_cycle_capacity"
CONF_BATTERY_STRINGS = "battery_strings"

CONF_ERRORS_BITMASK = "errors_bitmask"
CONF_OPERATION_MODE_BITMASK = "operation_mode_bitmask"

CONF_TOTAL_VOLTAGE_OVERVOLTAGE_PROTECTION = "total_voltage_overvoltage_protection"
CONF_TOTAL_VOLTAGE_UNDERVOLTAGE_PROTECTION = "total_voltage_undervoltage_protection"

CONF_CELL_VOLTAGE_OVERVOLTAGE_PROTECTION = "cell_voltage_overvoltage_protection"
CONF_CELL_VOLTAGE_OVERVOLTAGE_RECOVERY = "cell_voltage_overvoltage_recovery"
CONF_CELL_VOLTAGE_OVERVOLTAGE_DELAY = "cell_voltage_overvoltage_delay"

CONF_CELL_VOLTAGE_UNDERVOLTAGE_PROTECTION = "cell_voltage_undervoltage_protection"
CONF_CELL_VOLTAGE_UNDERVOLTAGE_RECOVERY = "cell_voltage_undervoltage_recovery"
CONF_CELL_VOLTAGE_UNDERVOLTAGE_DELAY = "cell_voltage_undervoltage_delay"

CONF_CELL_PRESSURE_DIFFERENCE_PROTECTION = "cell_pressure_difference_protection"

CONF_DISCHARGING_OVERCURRENT_PROTECTION = "discharging_overcurrent_protection"
CONF_DISCHARGING_OVERCURRENT_DELAY = "discharging_overcurrent_delay"

CONF_CHARGING_OVERCURRENT_PROTECTION = "charging_overcurrent_protection"
CONF_CHARGING_OVERCURRENT_DELAY = "charging_overcurrent_delay"

CONF_BALANCE_STARTING_VOLTAGE = "balance_starting_voltage"
CONF_BALANCE_OPENING_PRESSURE_DIFFERENCE = "balance_opening_pressure_difference"

CONF_POWER_TUBE_TEMPERATURE_PROTECTION = "power_tube_temperature_protection"
CONF_POWER_TUBE_TEMPERATURE_RECOVERY = "power_tube_temperature_recovery"

CONF_TEMPERATURE_SENSOR_TEMPERATURE_PROTECTION = (
    "temperature_sensor_temperature_protection"
)
CONF_TEMPERATURE_SENSOR_TEMPERATURE_RECOVERY = "temperature_sensor_temperature_recovery"
CONF_TEMPERATURE_SENSOR_TEMPERATURE_DIFFERENCE_PROTECTION = (
    "temperature_sensor_temperature_difference_protection"
)

CONF_CHARGING_HIGH_TEMPERATURE_PROTECTION = "charging_high_temperature_protection"
CONF_DISCHARGING_HIGH_TEMPERATURE_PROTECTION = "discharging_high_temperature_protection"

CONF_CHARGING_LOW_TEMPERATURE_PROTECTION = "charging_low_temperature_protection"
CONF_CHARGING_LOW_TEMPERATURE_RECOVERY = "charging_low_temperature_recovery"
CONF_DISCHARGING_LOW_TEMPERATURE_PROTECTION = "discharging_low_temperature_protection"
CONF_DISCHARGING_LOW_TEMPERATURE_RECOVERY = "discharging_low_temperature_recovery"

# r/w
# CONF_BATTERY_STRINGS = "battery_strings"
# CONF_BATTERY_CAPACITY = "battery_capacity"

CONF_CURRENT_CALIBRATION = "current_calibration"
CONF_DEVICE_ADDRESS = "device_address"
CONF_SLEEP_WAIT_TIME = "sleep_wait_time"
CONF_ALARM_LOW_VOLUME = "alarm_low_volume"
CONF_MANUFACTURING_DATE = "manufacturing_date"
CONF_TOTAL_RUNTIME = "total_runtime"
CONF_START_CURRENT_CALIBRATION = "start_current_calibration"
CONF_ACTUAL_BATTERY_CAPACITY = "actual_battery_capacity"
CONF_PROTOCOL_VERSION = "protocol_version"

ICON_BATTERY_STRINGS = "mdi:car-battery"
ICON_DEVICE_ADDRESS = "mdi:identifier"
ICON_ERRORS_BITMASK = "mdi:alert-circle-outline"
ICON_OPERATION_MODE_BITMASK = "mdi:heart-pulse"

UNIT_SECONDS = "s"
UNIT_HOURS = "h"
UNIT_AMPERE_HOURS = "Ah"

CELLS = [
    CONF_CELL_VOLTAGE_1,
    CONF_CELL_VOLTAGE_2,
    CONF_CELL_VOLTAGE_3,
    CONF_CELL_VOLTAGE_4,
    CONF_CELL_VOLTAGE_5,
    CONF_CELL_VOLTAGE_6,
    CONF_CELL_VOLTAGE_7,
    CONF_CELL_VOLTAGE_8,
    CONF_CELL_VOLTAGE_9,
    CONF_CELL_VOLTAGE_10,
    CONF_CELL_VOLTAGE_11,
    CONF_CELL_VOLTAGE_12,
    CONF_CELL_VOLTAGE_13,
    CONF_CELL_VOLTAGE_14,
    CONF_CELL_VOLTAGE_15,
    CONF_CELL_VOLTAGE_16,
    CONF_CELL_VOLTAGE_17,
    CONF_CELL_VOLTAGE_18,
    CONF_CELL_VOLTAGE_19,
    CONF_CELL_VOLTAGE_20,
    CONF_CELL_VOLTAGE_21,
    CONF_CELL_VOLTAGE_22,
    CONF_CELL_VOLTAGE_23,
    CONF_CELL_VOLTAGE_24,
]

SENSORS = [
    CONF_POWER_TUBE_TEMPERATURE,
    CONF_TEMPERATURE_SENSOR_1,
    CONF_TEMPERATURE_SENSOR_2,
    CONF_TOTAL_VOLTAGE,
    CONF_CURRENT,
    CONF_CAPACITY_REMAINING,
    CONF_TEMPERATURE_SENSORS,
    CONF_CHARGING_CYCLES,
    CONF_TOTAL_CHARGING_CYCLE_CAPACITY,
    CONF_BATTERY_STRINGS,
    CONF_ERRORS_BITMASK,
    CONF_OPERATION_MODE_BITMASK,
    CONF_TOTAL_VOLTAGE_OVERVOLTAGE_PROTECTION,
    CONF_TOTAL_VOLTAGE_UNDERVOLTAGE_PROTECTION,
    CONF_CELL_VOLTAGE_OVERVOLTAGE_PROTECTION,
    CONF_CELL_VOLTAGE_OVERVOLTAGE_RECOVERY,
    CONF_CELL_VOLTAGE_OVERVOLTAGE_DELAY,
    CONF_CELL_VOLTAGE_UNDERVOLTAGE_PROTECTION,
    CONF_CELL_VOLTAGE_UNDERVOLTAGE_RECOVERY,
    CONF_CELL_VOLTAGE_UNDERVOLTAGE_DELAY,
    CONF_CELL_PRESSURE_DIFFERENCE_PROTECTION,
    CONF_DISCHARGING_OVERCURRENT_PROTECTION,
    CONF_DISCHARGING_OVERCURRENT_DELAY,
    CONF_CHARGING_OVERCURRENT_PROTECTION,
    CONF_CHARGING_OVERCURRENT_DELAY,
    CONF_BALANCE_STARTING_VOLTAGE,
    CONF_BALANCE_OPENING_PRESSURE_DIFFERENCE,
    CONF_POWER_TUBE_TEMPERATURE_PROTECTION,
    CONF_POWER_TUBE_TEMPERATURE_RECOVERY,
    CONF_TEMPERATURE_SENSOR_TEMPERATURE_PROTECTION,
    CONF_TEMPERATURE_SENSOR_TEMPERATURE_RECOVERY,
    CONF_TEMPERATURE_SENSOR_TEMPERATURE_DIFFERENCE_PROTECTION,
    CONF_CHARGING_HIGH_TEMPERATURE_PROTECTION,
    CONF_DISCHARGING_HIGH_TEMPERATURE_PROTECTION,
    CONF_CHARGING_LOW_TEMPERATURE_PROTECTION,
    CONF_CHARGING_LOW_TEMPERATURE_RECOVERY,
    CONF_DISCHARGING_LOW_TEMPERATURE_PROTECTION,
    CONF_DISCHARGING_LOW_TEMPERATURE_RECOVERY,
    CONF_CURRENT_CALIBRATION,
    CONF_DEVICE_ADDRESS,
    CONF_SLEEP_WAIT_TIME,
    CONF_ALARM_LOW_VOLUME,
    CONF_MANUFACTURING_DATE,
    CONF_TOTAL_RUNTIME,
    CONF_START_CURRENT_CALIBRATION,
    CONF_ACTUAL_BATTERY_CAPACITY,
    CONF_PROTOCOL_VERSION,
]

CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(CONF_JK_BMS_ID): cv.use_id(JkBms),
        cv.Optional(CONF_CELL_VOLTAGE_1): sensor.sensor_schema(
            UNIT_VOLT, ICON_EMPTY, 3, DEVICE_CLASS_VOLTAGE, STATE_CLASS_MEASUREMENT
        ),
        cv.Optional(CONF_CELL_VOLTAGE_2): sensor.sensor_schema(
            UNIT_VOLT, ICON_EMPTY, 3, DEVICE_CLASS_VOLTAGE, STATE_CLASS_MEASUREMENT
        ),
        cv.Optional(CONF_CELL_VOLTAGE_3): sensor.sensor_schema(
            UNIT_VOLT, ICON_EMPTY, 3, DEVICE_CLASS_VOLTAGE, STATE_CLASS_MEASUREMENT
        ),
        cv.Optional(CONF_CELL_VOLTAGE_4): sensor.sensor_schema(
            UNIT_VOLT, ICON_EMPTY, 3, DEVICE_CLASS_VOLTAGE, STATE_CLASS_MEASUREMENT
        ),
        cv.Optional(CONF_CELL_VOLTAGE_5): sensor.sensor_schema(
            UNIT_VOLT, ICON_EMPTY, 3, DEVICE_CLASS_VOLTAGE, STATE_CLASS_MEASUREMENT
        ),
        cv.Optional(CONF_CELL_VOLTAGE_6): sensor.sensor_schema(
            UNIT_VOLT, ICON_EMPTY, 3, DEVICE_CLASS_VOLTAGE, STATE_CLASS_MEASUREMENT
        ),
        cv.Optional(CONF_CELL_VOLTAGE_7): sensor.sensor_schema(
            UNIT_VOLT, ICON_EMPTY, 3, DEVICE_CLASS_VOLTAGE, STATE_CLASS_MEASUREMENT
        ),
        cv.Optional(CONF_CELL_VOLTAGE_8): sensor.sensor_schema(
            UNIT_VOLT, ICON_EMPTY, 3, DEVICE_CLASS_VOLTAGE, STATE_CLASS_MEASUREMENT
        ),
        cv.Optional(CONF_CELL_VOLTAGE_9): sensor.sensor_schema(
            UNIT_VOLT, ICON_EMPTY, 3, DEVICE_CLASS_VOLTAGE, STATE_CLASS_MEASUREMENT
        ),
        cv.Optional(CONF_CELL_VOLTAGE_10): sensor.sensor_schema(
            UNIT_VOLT, ICON_EMPTY, 3, DEVICE_CLASS_VOLTAGE, STATE_CLASS_MEASUREMENT
        ),
        cv.Optional(CONF_CELL_VOLTAGE_11): sensor.sensor_schema(
            UNIT_VOLT, ICON_EMPTY, 3, DEVICE_CLASS_VOLTAGE, STATE_CLASS_MEASUREMENT
        ),
        cv.Optional(CONF_CELL_VOLTAGE_12): sensor.sensor_schema(
            UNIT_VOLT, ICON_EMPTY, 3, DEVICE_CLASS_VOLTAGE, STATE_CLASS_MEASUREMENT
        ),
        cv.Optional(CONF_CELL_VOLTAGE_13): sensor.sensor_schema(
            UNIT_VOLT, ICON_EMPTY, 3, DEVICE_CLASS_VOLTAGE, STATE_CLASS_MEASUREMENT
        ),
        cv.Optional(CONF_CELL_VOLTAGE_14): sensor.sensor_schema(
            UNIT_VOLT, ICON_EMPTY, 3, DEVICE_CLASS_VOLTAGE, STATE_CLASS_MEASUREMENT
        ),
        cv.Optional(CONF_CELL_VOLTAGE_15): sensor.sensor_schema(
            UNIT_VOLT, ICON_EMPTY, 3, DEVICE_CLASS_VOLTAGE, STATE_CLASS_MEASUREMENT
        ),
        cv.Optional(CONF_CELL_VOLTAGE_16): sensor.sensor_schema(
            UNIT_VOLT, ICON_EMPTY, 3, DEVICE_CLASS_VOLTAGE, STATE_CLASS_MEASUREMENT
        ),
        cv.Optional(CONF_CELL_VOLTAGE_17): sensor.sensor_schema(
            UNIT_VOLT, ICON_EMPTY, 3, DEVICE_CLASS_VOLTAGE, STATE_CLASS_MEASUREMENT
        ),
        cv.Optional(CONF_CELL_VOLTAGE_18): sensor.sensor_schema(
            UNIT_VOLT, ICON_EMPTY, 3, DEVICE_CLASS_VOLTAGE, STATE_CLASS_MEASUREMENT
        ),
        cv.Optional(CONF_CELL_VOLTAGE_19): sensor.sensor_schema(
            UNIT_VOLT, ICON_EMPTY, 3, DEVICE_CLASS_VOLTAGE, STATE_CLASS_MEASUREMENT
        ),
        cv.Optional(CONF_CELL_VOLTAGE_20): sensor.sensor_schema(
            UNIT_VOLT, ICON_EMPTY, 3, DEVICE_CLASS_VOLTAGE, STATE_CLASS_MEASUREMENT
        ),
        cv.Optional(CONF_CELL_VOLTAGE_21): sensor.sensor_schema(
            UNIT_VOLT, ICON_EMPTY, 3, DEVICE_CLASS_VOLTAGE, STATE_CLASS_MEASUREMENT
        ),
        cv.Optional(CONF_CELL_VOLTAGE_22): sensor.sensor_schema(
            UNIT_VOLT, ICON_EMPTY, 3, DEVICE_CLASS_VOLTAGE, STATE_CLASS_MEASUREMENT
        ),
        cv.Optional(CONF_CELL_VOLTAGE_23): sensor.sensor_schema(
            UNIT_VOLT, ICON_EMPTY, 3, DEVICE_CLASS_VOLTAGE, STATE_CLASS_MEASUREMENT
        ),
        cv.Optional(CONF_CELL_VOLTAGE_24): sensor.sensor_schema(
            UNIT_VOLT, ICON_EMPTY, 3, DEVICE_CLASS_VOLTAGE, STATE_CLASS_MEASUREMENT
        ),
        cv.Optional(CONF_POWER_TUBE_TEMPERATURE): sensor.sensor_schema(
            UNIT_CELSIUS,
            ICON_EMPTY,
            0,
            DEVICE_CLASS_TEMPERATURE,
            STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional(CONF_TEMPERATURE_SENSOR_1): sensor.sensor_schema(
            UNIT_CELSIUS,
            ICON_EMPTY,
            0,
            DEVICE_CLASS_TEMPERATURE,
            STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional(CONF_TEMPERATURE_SENSOR_2): sensor.sensor_schema(
            UNIT_CELSIUS,
            ICON_EMPTY,
            0,
            DEVICE_CLASS_TEMPERATURE,
            STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional(CONF_TOTAL_VOLTAGE): sensor.sensor_schema(
            UNIT_VOLT, ICON_EMPTY, 2, DEVICE_CLASS_VOLTAGE, STATE_CLASS_MEASUREMENT
        ),
        cv.Optional(CONF_CURRENT): sensor.sensor_schema(
            UNIT_AMPERE,
            ICON_EMPTY,
            2,
            DEVICE_CLASS_CURRENT,
            STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional(CONF_CAPACITY_REMAINING): sensor.sensor_schema(
            UNIT_PERCENT,
            ICON_EMPTY,
            0,
            DEVICE_CLASS_EMPTY,
            STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional(CONF_TEMPERATURE_SENSORS): sensor.sensor_schema(
            UNIT_EMPTY,
            ICON_EMPTY,
            0,
            DEVICE_CLASS_EMPTY,
            STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional(CONF_CHARGING_CYCLES): sensor.sensor_schema(
            UNIT_EMPTY,
            ICON_EMPTY,
            0,
            DEVICE_CLASS_EMPTY,
            STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional(CONF_TOTAL_CHARGING_CYCLE_CAPACITY): sensor.sensor_schema(
            UNIT_EMPTY,
            ICON_EMPTY,
            0,
            DEVICE_CLASS_EMPTY,
            STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional(CONF_BATTERY_STRINGS): sensor.sensor_schema(
            UNIT_EMPTY,
            ICON_BATTERY_STRINGS,
            0,
            DEVICE_CLASS_EMPTY,
            STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional(CONF_ERRORS_BITMASK): sensor.sensor_schema(
            UNIT_EMPTY,
            ICON_ERRORS_BITMASK,
            0,
            DEVICE_CLASS_EMPTY,
            STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional(CONF_OPERATION_MODE_BITMASK): sensor.sensor_schema(
            UNIT_EMPTY,
            ICON_OPERATION_MODE_BITMASK,
            0,
            DEVICE_CLASS_EMPTY,
            STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional(CONF_TOTAL_VOLTAGE_OVERVOLTAGE_PROTECTION): sensor.sensor_schema(
            UNIT_VOLT, ICON_EMPTY, 2, DEVICE_CLASS_VOLTAGE, STATE_CLASS_MEASUREMENT
        ),
        cv.Optional(CONF_TOTAL_VOLTAGE_UNDERVOLTAGE_PROTECTION): sensor.sensor_schema(
            UNIT_VOLT, ICON_EMPTY, 2, DEVICE_CLASS_VOLTAGE, STATE_CLASS_MEASUREMENT
        ),
        cv.Optional(CONF_CELL_VOLTAGE_OVERVOLTAGE_PROTECTION): sensor.sensor_schema(
            UNIT_VOLT, ICON_EMPTY, 3, DEVICE_CLASS_VOLTAGE, STATE_CLASS_MEASUREMENT
        ),
        cv.Optional(CONF_CELL_VOLTAGE_OVERVOLTAGE_RECOVERY): sensor.sensor_schema(
            UNIT_VOLT, ICON_EMPTY, 3, DEVICE_CLASS_VOLTAGE, STATE_CLASS_MEASUREMENT
        ),
        cv.Optional(CONF_CELL_VOLTAGE_OVERVOLTAGE_DELAY): sensor.sensor_schema(
            UNIT_SECONDS,
            ICON_TIMELAPSE,
            0,
            DEVICE_CLASS_EMPTY,
            STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional(CONF_CELL_VOLTAGE_UNDERVOLTAGE_PROTECTION): sensor.sensor_schema(
            UNIT_VOLT, ICON_EMPTY, 3, DEVICE_CLASS_VOLTAGE, STATE_CLASS_MEASUREMENT
        ),
        cv.Optional(CONF_CELL_VOLTAGE_UNDERVOLTAGE_RECOVERY): sensor.sensor_schema(
            UNIT_VOLT, ICON_EMPTY, 3, DEVICE_CLASS_VOLTAGE, STATE_CLASS_MEASUREMENT
        ),
        cv.Optional(CONF_CELL_VOLTAGE_UNDERVOLTAGE_DELAY): sensor.sensor_schema(
            UNIT_SECONDS,
            ICON_TIMELAPSE,
            0,
            DEVICE_CLASS_EMPTY,
            STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional(CONF_CELL_PRESSURE_DIFFERENCE_PROTECTION): sensor.sensor_schema(
            UNIT_VOLT, ICON_EMPTY, 3, DEVICE_CLASS_VOLTAGE, STATE_CLASS_MEASUREMENT
        ),
        cv.Optional(CONF_DISCHARGING_OVERCURRENT_PROTECTION): sensor.sensor_schema(
            UNIT_AMPERE,
            ICON_EMPTY,
            0,
            DEVICE_CLASS_CURRENT,
            STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional(CONF_DISCHARGING_OVERCURRENT_DELAY): sensor.sensor_schema(
            UNIT_SECONDS,
            ICON_TIMELAPSE,
            0,
            DEVICE_CLASS_EMPTY,
            STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional(CONF_CHARGING_OVERCURRENT_PROTECTION): sensor.sensor_schema(
            UNIT_AMPERE,
            ICON_EMPTY,
            0,
            DEVICE_CLASS_CURRENT,
            STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional(CONF_CHARGING_OVERCURRENT_DELAY): sensor.sensor_schema(
            UNIT_SECONDS,
            ICON_TIMELAPSE,
            0,
            DEVICE_CLASS_EMPTY,
            STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional(CONF_BALANCE_STARTING_VOLTAGE): sensor.sensor_schema(
            UNIT_VOLT, ICON_EMPTY, 3, DEVICE_CLASS_VOLTAGE, STATE_CLASS_MEASUREMENT
        ),
        cv.Optional(CONF_BALANCE_OPENING_PRESSURE_DIFFERENCE): sensor.sensor_schema(
            UNIT_VOLT, ICON_EMPTY, 3, DEVICE_CLASS_VOLTAGE, STATE_CLASS_MEASUREMENT
        ),
        cv.Optional(CONF_POWER_TUBE_TEMPERATURE_PROTECTION): sensor.sensor_schema(
            UNIT_CELSIUS,
            ICON_EMPTY,
            0,
            DEVICE_CLASS_TEMPERATURE,
            STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional(CONF_POWER_TUBE_TEMPERATURE_RECOVERY): sensor.sensor_schema(
            UNIT_CELSIUS,
            ICON_EMPTY,
            0,
            DEVICE_CLASS_TEMPERATURE,
            STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional(
            CONF_TEMPERATURE_SENSOR_TEMPERATURE_PROTECTION
        ): sensor.sensor_schema(
            UNIT_CELSIUS,
            ICON_EMPTY,
            0,
            DEVICE_CLASS_TEMPERATURE,
            STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional(CONF_TEMPERATURE_SENSOR_TEMPERATURE_RECOVERY): sensor.sensor_schema(
            UNIT_CELSIUS,
            ICON_EMPTY,
            0,
            DEVICE_CLASS_TEMPERATURE,
            STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional(
            CONF_TEMPERATURE_SENSOR_TEMPERATURE_DIFFERENCE_PROTECTION
        ): sensor.sensor_schema(
            UNIT_CELSIUS,
            ICON_EMPTY,
            0,
            DEVICE_CLASS_TEMPERATURE,
            STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional(CONF_CHARGING_HIGH_TEMPERATURE_PROTECTION): sensor.sensor_schema(
            UNIT_CELSIUS,
            ICON_EMPTY,
            0,
            DEVICE_CLASS_TEMPERATURE,
            STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional(CONF_DISCHARGING_HIGH_TEMPERATURE_PROTECTION): sensor.sensor_schema(
            UNIT_CELSIUS,
            ICON_EMPTY,
            0,
            DEVICE_CLASS_TEMPERATURE,
            STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional(CONF_CHARGING_LOW_TEMPERATURE_PROTECTION): sensor.sensor_schema(
            UNIT_CELSIUS,
            ICON_EMPTY,
            0,
            DEVICE_CLASS_TEMPERATURE,
            STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional(CONF_CHARGING_LOW_TEMPERATURE_RECOVERY): sensor.sensor_schema(
            UNIT_CELSIUS,
            ICON_EMPTY,
            0,
            DEVICE_CLASS_TEMPERATURE,
            STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional(CONF_DISCHARGING_LOW_TEMPERATURE_PROTECTION): sensor.sensor_schema(
            UNIT_CELSIUS,
            ICON_EMPTY,
            0,
            DEVICE_CLASS_TEMPERATURE,
            STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional(CONF_DISCHARGING_LOW_TEMPERATURE_RECOVERY): sensor.sensor_schema(
            UNIT_CELSIUS,
            ICON_EMPTY,
            0,
            DEVICE_CLASS_TEMPERATURE,
            STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional(CONF_CURRENT_CALIBRATION): sensor.sensor_schema(
            UNIT_AMPERE,
            ICON_EMPTY,
            3,
            DEVICE_CLASS_CURRENT,
            STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional(CONF_DEVICE_ADDRESS): sensor.sensor_schema(
            UNIT_EMPTY,
            ICON_DEVICE_ADDRESS,
            0,
            DEVICE_CLASS_EMPTY,
            STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional(CONF_SLEEP_WAIT_TIME): sensor.sensor_schema(
            UNIT_SECONDS,
            ICON_TIMELAPSE,
            0,
            DEVICE_CLASS_EMPTY,
            STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional(CONF_ALARM_LOW_VOLUME): sensor.sensor_schema(
            UNIT_PERCENT,
            ICON_EMPTY,
            0,
            DEVICE_CLASS_EMPTY,
            STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional(CONF_MANUFACTURING_DATE): sensor.sensor_schema(
            UNIT_EMPTY,
            ICON_EMPTY,
            0,
            DEVICE_CLASS_EMPTY,
            STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional(CONF_TOTAL_RUNTIME): sensor.sensor_schema(
            UNIT_HOURS,
            ICON_TIMELAPSE,
            0,
            DEVICE_CLASS_EMPTY,
            STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional(CONF_START_CURRENT_CALIBRATION): sensor.sensor_schema(
            UNIT_EMPTY,
            ICON_EMPTY,
            0,
            DEVICE_CLASS_EMPTY,
            STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional(CONF_ACTUAL_BATTERY_CAPACITY): sensor.sensor_schema(
            UNIT_AMPERE_HOURS,
            ICON_EMPTY,
            0,
            DEVICE_CLASS_EMPTY,
            STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional(CONF_PROTOCOL_VERSION): sensor.sensor_schema(
            UNIT_EMPTY,
            ICON_EMPTY,
            0,
            DEVICE_CLASS_EMPTY,
            STATE_CLASS_MEASUREMENT,
        ),
    }
)


def to_code(config):
    hub = yield cg.get_variable(config[CONF_JK_BMS_ID])
    for i, key in enumerate(CELLS):
        if key in config:
            conf = config[key]
            sens = yield sensor.new_sensor(conf)
            cg.add(hub.set_cell_voltage_sensor(i, sens))
    for key in SENSORS:
        if key in config:
            conf = config[key]
            sens = yield sensor.new_sensor(conf)
            cg.add(getattr(hub, f"set_{key}_sensor")(sens))
