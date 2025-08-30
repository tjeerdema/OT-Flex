import json
from opentrons import protocol_api, types

metadata = {
    "protocolName": "Q5 PCR (Tm65+Tm68) + DpnI",
    "author": "Evan Tjeerdema - SIO",
    "description": "PCR for HiFi assembly. PCR off sequence fragments & plasmid. 10C hold at the end. Oligos and DNA fragments held at RT. Q5 and DpnI held at 10C. ",
    "created": "2025-07-29T05:49:24.600Z",
    "lastModified": "2025-08-30T02:54:16.470Z",
    "protocolDesigner": "8.5.2",
    "source": "Protocol Designer",
}

requirements = {"robotType": "Flex", "apiLevel": "2.24"}

def run(protocol: protocol_api.ProtocolContext) -> None:
    # Load Modules:
    thermocycler_module_1 = protocol.load_module("thermocyclerModuleV2", "B1")
    heater_shaker_module_1 = protocol.load_module("heaterShakerModuleV1", "D1")
    temperature_module_1 = protocol.load_module("temperatureModuleV2", "C1")

    # Load Adapters:
    aluminum_block_1 = temperature_module_1.load_adapter(
        "opentrons_96_well_aluminum_block",
        namespace="opentrons",
        version=1,
    )

    # Load Labware:
    tip_rack_1 = protocol.load_labware(
        "opentrons_flex_96_filtertiprack_50ul",
        location="A2",
        namespace="opentrons",
        version=1,
    )
    well_plate_1 = thermocycler_module_1.load_labware(
        "opentrons_96_wellplate_200ul_pcr_full_skirt",
        label="Opentrons Tough 96 Well Plate 200 µL PCR Full Skirt (1)",
        namespace="opentrons",
        version=2,
    )
    well_plate_2 = aluminum_block_1.load_labware(
        "armadillo_96_wellplate_200ul_pcr_full_skirt",
        label="(Retired) Armadillo 96 Well Plate 200 µL PCR Full Skirt",
        namespace="opentrons",
        version=3,
    )
    tip_rack_2 = protocol.load_labware(
        "opentrons_flex_96_filtertiprack_50ul",
        location="A3",
        label="Opentrons Flex 96 Filter Tip Rack 50 µL (1)",
        namespace="opentrons",
        version=1,
    )
    tip_rack_3 = protocol.load_labware(
        "opentrons_flex_96_filtertiprack_50ul",
        location="B2",
        label="Opentrons Flex 96 Filter Tip Rack 50 µL (2)",
        namespace="opentrons",
        version=1,
    )

    # Load Pipettes:
    pipette_right = protocol.load_instrument(
        "flex_1channel_50", "right", tip_racks=[tip_rack_1, tip_rack_2, tip_rack_3],
    )
    pipette_left = protocol.load_instrument(
        "flex_8channel_50", "left", tip_racks=[tip_rack_1, tip_rack_2, tip_rack_3],
    )

    # Load Waste Chute:
    waste_chute = protocol.load_waste_chute()

    # Define Liquids:
    liquid_3 = protocol.define_liquid(
        "Q5MM",
        description="Appropriate volume of Q5MM",
        display_color="#ff4f4fff",
    )
    liquid_4 = protocol.define_liquid(
        "HiFi assembly MM",
        description="Use at 2X",
        display_color="#ff9900",
    )
    liquid_5 = protocol.define_liquid(
        "DNA fragment - 1ng/ul",
        display_color="#14a502ff",
    )
    liquid_6 = protocol.define_liquid(
        "Plasmid template - 1ng/ul",
        display_color="#0028ffff",
    )
    liquid_7 = protocol.define_liquid(
        "NF H2O",
        display_color="#7eff42",
    )
    liquid_8 = protocol.define_liquid(
        "PRIMER MIX",
        display_color="#ff9900ff",
    )
    liquid_9 = protocol.define_liquid(
        "FP 10µM -Tm58",
        display_color="#b925ff",
    )
    liquid_10 = protocol.define_liquid(
        "FP 10µM -Tm62",
        display_color="#50d5ffff",
    )
    liquid_11 = protocol.define_liquid(
        "FP 10µM -Tm66",
        display_color="#ff9900ff",
    )
    liquid_12 = protocol.define_liquid(
        "RP 10µM -Tm58",
        display_color="#ff4f4fff",
    )
    liquid_13 = protocol.define_liquid(
        "RP 10µM -Tm62",
        display_color="#ff80f5ff",
    )
    liquid_14 = protocol.define_liquid(
        "RP 10µM -Tm66",
        display_color="#b925ffff",
    )
    liquid_15 = protocol.define_liquid(
        "CYCLIN-CD5",
        display_color="#7eff42",
    )
    liquid_16 = protocol.define_liquid(
        "MTA-CD5",
        display_color="#ff4f4f",
    )
    liquid_17 = protocol.define_liquid(
        "LpPU-CD5",
        display_color="#b925ff",
    )
    liquid_18 = protocol.define_liquid(
        "LpGS-CD5",
        display_color="#ffd600",
    )
    liquid_19 = protocol.define_liquid(
        "LVP_MINOS_LINEAR_BACKBONE",
        display_color="#b925ffff",
    )
    liquid_20 = protocol.define_liquid(
        "DpnI",
        display_color="#ff9900",
    )
    liquid_21 = protocol.define_liquid(
        "rCutsmart 10X",
        display_color="#50d5ff",
    )
    liquid_22 = protocol.define_liquid(
        "F1",
        display_color="#ff80f5",
    )
    liquid_23 = protocol.define_liquid(
        "R1",
        display_color="#7eff42",
    )
    liquid_24 = protocol.define_liquid(
        "F2",
        display_color="#ff4f4f",
    )
    liquid_25 = protocol.define_liquid(
        "R2",
        display_color="#b925ff",
    )

    # Load Liquids:
    well_plate_2.load_liquid(
        wells=["A12", "B12", "C12", "D12"],
        liquid=liquid_3,
        volume=125,
    )
    well_plate_2.load_liquid(
        wells=["H12"],
        liquid=liquid_20,
        volume=10,
    )
    well_plate_2.load_liquid(
        wells=["G12"],
        liquid=liquid_21,
        volume=50,
    )
    well_plate_2.load_liquid(
        wells=["A11"],
        liquid=liquid_22,
        volume=20,
    )
    well_plate_2.load_liquid(
        wells=["B11"],
        liquid=liquid_23,
        volume=20,
    )
    well_plate_2.load_liquid(
        wells=["C11"],
        liquid=liquid_24,
        volume=20,
    )
    well_plate_2.load_liquid(
        wells=["D11"],
        liquid=liquid_25,
        volume=20,
    )
    well_plate_2.load_liquid(
        wells=["H11"],
        liquid=liquid_6,
        volume=10,
    )
    well_plate_2.load_liquid(
        wells=[
            "A10", "B10", "C10", "D10", "E10", "F10", "G10", "H10"
        ],
        liquid=liquid_7,
        volume=200,
    )

    # Load Liquid Classes:
    glycerol_50_base_class = protocol.get_liquid_class("glycerol_50")
    water_base_class = protocol.get_liquid_class("water")

    # PROTOCOL STEPS

    # Step 1:
    temperature_module_1.start_set_temperature(10)

    # Step 2:
    temperature_module_1.start_set_temperature(10)

    # Step 3:
    thermocycler_module_1.open_lid()
    thermocycler_module_1.set_block_temperature(10)

    # Step 4:
    pipette_right.distribute_with_liquid_class(
        volume=25,
        source=[well_plate_2["A12"]],
        dest=[well_plate_1["A1"], well_plate_1["B1"]],
        new_tip="once",
        trash_location=waste_chute,
        keep_last_tip=True,
        liquid_class=protocol.define_liquid_class(
            name="distribute_step_4",
            base_liquid_class=glycerol_50_base_class,
            properties={"flex_1channel_50": {"opentrons/opentrons_flex_96_filtertiprack_50ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0), (1, -0.2), (10, 0.1), (50, -0.2)],
                    "delay": {"enabled": True, "duration": 1},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 4,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 4,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 25)],
                    "delay": {"enabled": True, "duration": 0.5},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 4,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 4,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": True, "location": "trash", "flow_rate": 25},
                    },
                    "correction_by_volume": [(0, 0), (1, -0.2), (10, 0.1), (50, -0.2)],
                    "push_out_by_volume": [(0, 3.9)],
                    "mix": {"enabled": False},
                },
                "multi_dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 25)],
                    "delay": {"enabled": True, "duration": 0.5},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 4,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 4,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": True, "location": "trash", "flow_rate": 25},
                    },
                    "correction_by_volume": [(0, 0), (1, -0.2), (10, 0.1), (50, -0.2)],
                    "conditioning_by_volume": [(0, 0)],
                    "disposal_by_volume": [(0, 0)],
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 5:
    pipette_right.distribute_with_liquid_class(
        volume=2.5,
        source=[well_plate_2["A11"]],
        dest=[well_plate_1["A1"], well_plate_1["B1"]],
        new_tip="once",
        trash_location=waste_chute,
        keep_last_tip=True,
        liquid_class=protocol.define_liquid_class(
            name="distribute_step_5",
            base_liquid_class=water_base_class,
            properties={"flex_1channel_50": {"opentrons/opentrons_flex_96_filtertiprack_50ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 25.3)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": True, "duration": 0.2},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 100,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 43)],
                    "delay": {"enabled": True, "duration": 0.2},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 100,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0.1)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": True, "location": "trash", "flow_rate": 50},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 7)],
                    "mix": {"enabled": False},
                },
                "multi_dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 43)],
                    "delay": {"enabled": True, "duration": 0.2},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 100,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0.1)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": True, "location": "trash", "flow_rate": 50},
                    },
                    "correction_by_volume": [(0, 0)],
                    "conditioning_by_volume": [(0, 5)],
                    "disposal_by_volume": [(0, 5)],
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 6:
    pipette_right.transfer_with_liquid_class(
        volume=1,
        source=[well_plate_2["H11"], well_plate_2["H11"]],
        dest=[well_plate_1["A1"], well_plate_1["B1"]],
        new_tip="always",
        trash_location=waste_chute,
        keep_last_tip=True,
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_6",
            base_liquid_class=water_base_class,
            properties={"flex_1channel_50": {"opentrons/opentrons_flex_96_filtertiprack_50ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 33)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": True, "duration": 0.2},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 100,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0.1)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 33)],
                    "delay": {"enabled": True, "duration": 0.2},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 100,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0.1)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 7)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 7:
    pipette_right.distribute_with_liquid_class(
        volume=2.5,
        source=[well_plate_2["B11"]],
        dest=[well_plate_1["A1"], well_plate_1["B1"]],
        new_tip="once",
        trash_location=waste_chute,
        keep_last_tip=True,
        liquid_class=protocol.define_liquid_class(
            name="distribute_step_7",
            base_liquid_class=water_base_class,
            properties={"flex_1channel_50": {"opentrons/opentrons_flex_96_filtertiprack_50ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 25.3)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": True, "duration": 0.2},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 100,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 43)],
                    "delay": {"enabled": True, "duration": 0.2},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 100,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0.1)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": True, "location": "trash", "flow_rate": 50},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 7)],
                    "mix": {"enabled": False},
                },
                "multi_dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 43)],
                    "delay": {"enabled": True, "duration": 0.2},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 100,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0.1)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": True, "location": "trash", "flow_rate": 50},
                    },
                    "correction_by_volume": [(0, 0)],
                    "conditioning_by_volume": [(0, 5)],
                    "disposal_by_volume": [(0, 5)],
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 8:
    pipette_right.transfer_with_liquid_class(
        volume=19,
        source=[well_plate_2["A10"], well_plate_2["A10"]],
        dest=[well_plate_1["A1"], well_plate_1["B1"]],
        new_tip="always",
        trash_location=waste_chute,
        keep_last_tip=True,
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_8",
            base_liquid_class=water_base_class,
            properties={"flex_1channel_50": {"opentrons/opentrons_flex_96_filtertiprack_50ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 26.4)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": True, "duration": 0.2},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 100,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0.1)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
                    "delay": {"enabled": True, "duration": 0.2},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 100,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0.1)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 2)],
                    "mix": {"enabled": True, "repetitions": 5, "volume": 25},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 9:
    thermocycler_module_1.close_lid()
    thermocycler_module_1.set_lid_temperature(110)
    thermocycler_module_1.execute_profile(
        [
            {"temperature": 98, "hold_time_seconds": 30},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 65, "hold_time_seconds": 10},
            {"temperature": 72, "hold_time_seconds": 70},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 65, "hold_time_seconds": 10},
            {"temperature": 72, "hold_time_seconds": 70},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 65, "hold_time_seconds": 10},
            {"temperature": 72, "hold_time_seconds": 70},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 65, "hold_time_seconds": 10},
            {"temperature": 72, "hold_time_seconds": 70},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 65, "hold_time_seconds": 10},
            {"temperature": 72, "hold_time_seconds": 70},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 65, "hold_time_seconds": 10},
            {"temperature": 72, "hold_time_seconds": 70},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 65, "hold_time_seconds": 10},
            {"temperature": 72, "hold_time_seconds": 70},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 65, "hold_time_seconds": 10},
            {"temperature": 72, "hold_time_seconds": 70},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 65, "hold_time_seconds": 10},
            {"temperature": 72, "hold_time_seconds": 70},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 65, "hold_time_seconds": 10},
            {"temperature": 72, "hold_time_seconds": 70},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 65, "hold_time_seconds": 10},
            {"temperature": 72, "hold_time_seconds": 70},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 65, "hold_time_seconds": 10},
            {"temperature": 72, "hold_time_seconds": 70},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 65, "hold_time_seconds": 10},
            {"temperature": 72, "hold_time_seconds": 70},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 65, "hold_time_seconds": 10},
            {"temperature": 72, "hold_time_seconds": 70},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 65, "hold_time_seconds": 10},
            {"temperature": 72, "hold_time_seconds": 70},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 65, "hold_time_seconds": 10},
            {"temperature": 72, "hold_time_seconds": 70},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 65, "hold_time_seconds": 10},
            {"temperature": 72, "hold_time_seconds": 70},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 65, "hold_time_seconds": 10},
            {"temperature": 72, "hold_time_seconds": 70},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 65, "hold_time_seconds": 10},
            {"temperature": 72, "hold_time_seconds": 70},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 65, "hold_time_seconds": 10},
            {"temperature": 72, "hold_time_seconds": 70},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 65, "hold_time_seconds": 10},
            {"temperature": 72, "hold_time_seconds": 70},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 65, "hold_time_seconds": 10},
            {"temperature": 72, "hold_time_seconds": 70},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 65, "hold_time_seconds": 10},
            {"temperature": 72, "hold_time_seconds": 70},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 65, "hold_time_seconds": 10},
            {"temperature": 72, "hold_time_seconds": 70},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 65, "hold_time_seconds": 10},
            {"temperature": 72, "hold_time_seconds": 70},
            {"temperature": 72, "hold_time_seconds": 120},
        ],
        1,
        block_max_volume=50,
    )
    thermocycler_module_1.open_lid()
    thermocycler_module_1.set_block_temperature(10)
    thermocycler_module_1.set_lid_temperature(37)

    # Step 10:
    pipette_right.transfer_with_liquid_class(
        volume=55,
        source=[well_plate_1["A1"], well_plate_1["B1"]],
        dest=[well_plate_2["A1"], well_plate_2["B1"]],
        new_tip="always",
        trash_location=waste_chute,
        keep_last_tip=True,
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_10",
            base_liquid_class=water_base_class,
            properties={"flex_1channel_50": {"opentrons/opentrons_flex_96_filtertiprack_50ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 28.8)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": True, "duration": 0.2},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 100,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0.1)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
                    "delay": {"enabled": True, "duration": 0.2},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 100,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0.1)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 2)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 11:
    pipette_right.distribute_with_liquid_class(
        volume=25,
        source=[well_plate_2["A12"]],
        dest=[well_plate_1["C1"], well_plate_1["D1"]],
        new_tip="once",
        trash_location=waste_chute,
        keep_last_tip=True,
        liquid_class=protocol.define_liquid_class(
            name="distribute_step_11",
            base_liquid_class=glycerol_50_base_class,
            properties={"flex_1channel_50": {"opentrons/opentrons_flex_96_filtertiprack_50ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0), (1, -0.2), (10, 0.1), (50, -0.2)],
                    "delay": {"enabled": True, "duration": 1},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 4,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 4,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 25)],
                    "delay": {"enabled": True, "duration": 0.5},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 4,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 4,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": True, "location": "trash", "flow_rate": 25},
                    },
                    "correction_by_volume": [(0, 0), (1, -0.2), (10, 0.1), (50, -0.2)],
                    "push_out_by_volume": [(0, 3.9)],
                    "mix": {"enabled": False},
                },
                "multi_dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 25)],
                    "delay": {"enabled": True, "duration": 0.5},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 4,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 4,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": True, "location": "trash", "flow_rate": 25},
                    },
                    "correction_by_volume": [(0, 0), (1, -0.2), (10, 0.1), (50, -0.2)],
                    "conditioning_by_volume": [(0, 0)],
                    "disposal_by_volume": [(0, 0)],
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 12:
    pipette_right.distribute_with_liquid_class(
        volume=2.5,
        source=[well_plate_2["C11"]],
        dest=[well_plate_1["C1"], well_plate_1["D1"]],
        new_tip="once",
        trash_location=waste_chute,
        keep_last_tip=True,
        liquid_class=protocol.define_liquid_class(
            name="distribute_step_12",
            base_liquid_class=water_base_class,
            properties={"flex_1channel_50": {"opentrons/opentrons_flex_96_filtertiprack_50ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 25.3)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": True, "duration": 0.2},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 100,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 43)],
                    "delay": {"enabled": True, "duration": 0.2},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 100,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0.1)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": True, "location": "trash", "flow_rate": 50},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 7)],
                    "mix": {"enabled": False},
                },
                "multi_dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 43)],
                    "delay": {"enabled": True, "duration": 0.2},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 100,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0.1)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": True, "location": "trash", "flow_rate": 50},
                    },
                    "correction_by_volume": [(0, 0)],
                    "conditioning_by_volume": [(0, 5)],
                    "disposal_by_volume": [(0, 5)],
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 13:
    pipette_right.transfer_with_liquid_class(
        volume=1,
        source=[well_plate_2["H11"], well_plate_2["H11"]],
        dest=[well_plate_1["C1"], well_plate_1["D1"]],
        new_tip="always",
        trash_location=waste_chute,
        keep_last_tip=True,
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_13",
            base_liquid_class=water_base_class,
            properties={"flex_1channel_50": {"opentrons/opentrons_flex_96_filtertiprack_50ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 33)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": True, "duration": 0.2},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 100,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0.1)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 33)],
                    "delay": {"enabled": True, "duration": 0.2},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 100,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0.1)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 7)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 14:
    pipette_right.distribute_with_liquid_class(
        volume=2.5,
        source=[well_plate_2["D11"]],
        dest=[well_plate_1["C1"], well_plate_1["D1"]],
        new_tip="once",
        trash_location=waste_chute,
        keep_last_tip=True,
        liquid_class=protocol.define_liquid_class(
            name="distribute_step_14",
            base_liquid_class=water_base_class,
            properties={"flex_1channel_50": {"opentrons/opentrons_flex_96_filtertiprack_50ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 25.3)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": True, "duration": 0.2},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 100,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 43)],
                    "delay": {"enabled": True, "duration": 0.2},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 100,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0.1)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": True, "location": "trash", "flow_rate": 50},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 7)],
                    "mix": {"enabled": False},
                },
                "multi_dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 43)],
                    "delay": {"enabled": True, "duration": 0.2},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 100,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0.1)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": True, "location": "trash", "flow_rate": 50},
                    },
                    "correction_by_volume": [(0, 0)],
                    "conditioning_by_volume": [(0, 5)],
                    "disposal_by_volume": [(0, 5)],
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 15:
    pipette_right.transfer_with_liquid_class(
        volume=19,
        source=[well_plate_2["B10"], well_plate_2["B10"]],
        dest=[well_plate_1["C1"], well_plate_1["D1"]],
        new_tip="always",
        trash_location=waste_chute,
        keep_last_tip=True,
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_15",
            base_liquid_class=water_base_class,
            properties={"flex_1channel_50": {"opentrons/opentrons_flex_96_filtertiprack_50ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 26.4)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": True, "duration": 0.2},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 100,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0.1)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
                    "delay": {"enabled": True, "duration": 0.2},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 100,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0.1)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 2)],
                    "mix": {"enabled": True, "repetitions": 5, "volume": 25},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 16:
    thermocycler_module_1.close_lid()
    thermocycler_module_1.set_lid_temperature(110)
    thermocycler_module_1.execute_profile(
        [
            {"temperature": 98, "hold_time_seconds": 30},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 68, "hold_time_seconds": 10},
            {"temperature": 72, "hold_time_seconds": 70},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 68, "hold_time_seconds": 10},
            {"temperature": 72, "hold_time_seconds": 70},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 68, "hold_time_seconds": 10},
            {"temperature": 72, "hold_time_seconds": 70},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 68, "hold_time_seconds": 10},
            {"temperature": 72, "hold_time_seconds": 70},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 68, "hold_time_seconds": 10},
            {"temperature": 72, "hold_time_seconds": 70},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 68, "hold_time_seconds": 10},
            {"temperature": 72, "hold_time_seconds": 70},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 68, "hold_time_seconds": 10},
            {"temperature": 72, "hold_time_seconds": 70},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 68, "hold_time_seconds": 10},
            {"temperature": 72, "hold_time_seconds": 70},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 68, "hold_time_seconds": 10},
            {"temperature": 72, "hold_time_seconds": 70},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 68, "hold_time_seconds": 10},
            {"temperature": 72, "hold_time_seconds": 70},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 68, "hold_time_seconds": 10},
            {"temperature": 72, "hold_time_seconds": 70},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 68, "hold_time_seconds": 10},
            {"temperature": 72, "hold_time_seconds": 70},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 68, "hold_time_seconds": 10},
            {"temperature": 72, "hold_time_seconds": 70},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 68, "hold_time_seconds": 10},
            {"temperature": 72, "hold_time_seconds": 70},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 68, "hold_time_seconds": 10},
            {"temperature": 72, "hold_time_seconds": 70},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 68, "hold_time_seconds": 10},
            {"temperature": 72, "hold_time_seconds": 70},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 68, "hold_time_seconds": 10},
            {"temperature": 72, "hold_time_seconds": 70},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 68, "hold_time_seconds": 10},
            {"temperature": 72, "hold_time_seconds": 70},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 68, "hold_time_seconds": 10},
            {"temperature": 72, "hold_time_seconds": 70},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 68, "hold_time_seconds": 10},
            {"temperature": 72, "hold_time_seconds": 70},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 68, "hold_time_seconds": 10},
            {"temperature": 72, "hold_time_seconds": 70},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 68, "hold_time_seconds": 10},
            {"temperature": 72, "hold_time_seconds": 70},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 68, "hold_time_seconds": 10},
            {"temperature": 72, "hold_time_seconds": 70},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 68, "hold_time_seconds": 10},
            {"temperature": 72, "hold_time_seconds": 70},
            {"temperature": 98, "hold_time_seconds": 10},
            {"temperature": 68, "hold_time_seconds": 10},
            {"temperature": 72, "hold_time_seconds": 70},
            {"temperature": 72, "hold_time_seconds": 120},
        ],
        1,
        block_max_volume=50,
    )
    thermocycler_module_1.open_lid()
    thermocycler_module_1.set_block_temperature(10)
    thermocycler_module_1.set_lid_temperature(37)

    # Step 17:
    pipette_right.transfer_with_liquid_class(
        volume=55,
        source=[well_plate_1["C1"], well_plate_1["D1"]],
        dest=[well_plate_2["C1"], well_plate_2["D1"]],
        new_tip="always",
        trash_location=waste_chute,
        keep_last_tip=True,
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_17",
            base_liquid_class=water_base_class,
            properties={"flex_1channel_50": {"opentrons/opentrons_flex_96_filtertiprack_50ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 28.8)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": True, "duration": 0.2},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 100,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0.1)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
                    "delay": {"enabled": True, "duration": 0.2},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 100,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0.1)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 2)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 18:
    pipette_right.transfer_with_liquid_class(
        volume=2,
        source=[well_plate_2["H12"], well_plate_2["H12"], well_plate_2["H12"], well_plate_2["H12"]],
        dest=[well_plate_2["A1"], well_plate_2["B1"], well_plate_2["C1"], well_plate_2["D1"]],
        new_tip="always",
        trash_location=waste_chute,
        keep_last_tip=True,
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_18",
            base_liquid_class=glycerol_50_base_class,
            properties={"flex_1channel_50": {"opentrons/opentrons_flex_96_filtertiprack_50ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 7.3)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0), (1, -0.2), (10, 0.1), (50, -0.2)],
                    "delay": {"enabled": True, "duration": 1},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 4,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 4,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 25)],
                    "delay": {"enabled": True, "duration": 0.5},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 4,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 4,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0), (1, -0.2), (10, 0.1), (50, -0.2)],
                    "push_out_by_volume": [(0, 11.7)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 19:
    pipette_right.transfer_with_liquid_class(
        volume=10,
        source=[well_plate_2["G12"], well_plate_2["G12"], well_plate_2["G12"], well_plate_2["G12"]],
        dest=[well_plate_2["A1"], well_plate_2["B1"], well_plate_2["C1"], well_plate_2["D1"]],
        new_tip="always",
        trash_location=waste_chute,
        keep_last_tip=True,
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_19",
            base_liquid_class=water_base_class,
            properties={"flex_1channel_50": {"opentrons/opentrons_flex_96_filtertiprack_50ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 24)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": True, "duration": 0.2},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 100,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0.1)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
                    "delay": {"enabled": True, "duration": 0.2},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 100,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0.1)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 2)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 20:
    pipette_right.transfer_with_liquid_class(
        volume=43,
        source=[well_plate_2["C10"], well_plate_2["C10"]],
        dest=[well_plate_2["A1"], well_plate_2["B1"]],
        new_tip="always",
        trash_location=waste_chute,
        keep_last_tip=True,
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_20",
            base_liquid_class=water_base_class,
            properties={"flex_1channel_50": {"opentrons/opentrons_flex_96_filtertiprack_50ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 33)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": True, "duration": 0.2},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 100,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0.1)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
                    "delay": {"enabled": True, "duration": 0.2},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 100,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0.1)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 2)],
                    "mix": {"enabled": True, "repetitions": 5, "volume": 45},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 21:
    pipette_right.transfer_with_liquid_class(
        volume=43,
        source=[well_plate_2["D10"], well_plate_2["D10"]],
        dest=[well_plate_2["C1"], well_plate_2["D1"]],
        new_tip="always",
        trash_location=waste_chute,
        keep_last_tip=True,
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_21",
            base_liquid_class=water_base_class,
            properties={"flex_1channel_50": {"opentrons/opentrons_flex_96_filtertiprack_50ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 33)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": True, "duration": 0.2},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 100,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0.1)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
                    "delay": {"enabled": True, "duration": 0.2},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 100,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0.1)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 2)],
                    "mix": {"enabled": True, "repetitions": 5, "volume": 45},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 22:
    pipette_right.transfer_with_liquid_class(
        volume=110,
        source=[well_plate_2["A1"], well_plate_2["B1"], well_plate_2["C1"], well_plate_2["D1"]],
        dest=[well_plate_1["E1"], well_plate_1["F1"], well_plate_1["G1"], well_plate_1["H1"]],
        new_tip="always",
        trash_location=waste_chute,
        keep_last_tip=True,
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_22",
            base_liquid_class=water_base_class,
            properties={"flex_1channel_50": {"opentrons/opentrons_flex_96_filtertiprack_50ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 31.3)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": True, "duration": 0.2},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 100,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0.1)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
                    "delay": {"enabled": True, "duration": 0.2},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 100,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0.1)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 50,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 2)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_right.drop_tip(waste_chute)

    # Step 23:
    thermocycler_module_1.close_lid()
    thermocycler_module_1.set_lid_temperature(110)
    thermocycler_module_1.execute_profile(
        [
            {"temperature": 37, "hold_time_seconds": 1800},
            {"temperature": 65, "hold_time_seconds": 1200},
        ],
        1,
        block_max_volume=100,
    )
    thermocycler_module_1.set_block_temperature(10)
    thermocycler_module_1.set_lid_temperature(37)

DESIGNER_APPLICATION = """{"robot":{"model":"OT-3 Standard"},"designerApplication":{"name":"opentrons/protocol-designer","version":"8.5.0","data":{"pipetteTiprackAssignments":{"63555313-4253-4347-be9c-8b6e64189bb7":["opentrons/opentrons_flex_96_filtertiprack_50ul/1"],"8e36439e-b289-4759-8202-396adc7c9436":["opentrons/opentrons_flex_96_filtertiprack_50ul/1"]},"dismissedWarnings":{"form":[],"timeline":[]},"ingredients":{"2":{"displayName":"Q5MM","description":"Appropriate volume of Q5MM","displayColor":"#ff4f4fff","liquidGroupId":"2","liquidClass":"glycerol50V1"},"3":{"displayName":"HiFi assembly MM","description":"Use at 2X","displayColor":"#ff9900","liquidGroupId":"3","liquidClass":"glycerol50V1"},"4":{"displayName":"DNA fragment - 1ng/ul","description":null,"displayColor":"#14a502ff","liquidGroupId":"4","liquidClass":"waterV1"},"5":{"displayName":"Plasmid template - 1ng/ul","description":null,"displayColor":"#0028ffff","liquidGroupId":"5","liquidClass":"waterV1"},"6":{"displayName":"NF H2O","description":null,"displayColor":"#7eff42","liquidGroupId":"6","liquidClass":"waterV1"},"7":{"displayName":"PRIMER MIX","description":null,"displayColor":"#ff9900ff","liquidGroupId":"7","liquidClass":"waterV1"},"8":{"displayName":"FP 10µM -Tm58","description":null,"displayColor":"#b925ff","liquidGroupId":"8","liquidClass":"waterV1"},"9":{"displayName":"FP 10µM -Tm62","description":null,"displayColor":"#50d5ffff","liquidGroupId":"9","liquidClass":"waterV1"},"10":{"displayName":"FP 10µM -Tm66","description":null,"displayColor":"#ff9900ff","liquidGroupId":"10","liquidClass":"waterV1"},"11":{"displayName":"RP 10µM -Tm58","description":null,"displayColor":"#ff4f4fff","liquidGroupId":"11","liquidClass":"waterV1"},"12":{"displayName":"RP 10µM -Tm62","description":null,"displayColor":"#ff80f5ff","liquidGroupId":"12","liquidClass":"waterV1"},"13":{"displayName":"RP 10µM -Tm66","description":null,"displayColor":"#b925ffff","liquidGroupId":"13","liquidClass":"waterV1"},"14":{"displayName":"CYCLIN-CD5","description":null,"displayColor":"#7eff42","liquidGroupId":"14","liquidClass":"waterV1"},"15":{"displayName":"MTA-CD5","description":null,"displayColor":"#ff4f4f","liquidGroupId":"15","liquidClass":"waterV1"},"16":{"displayName":"LpPU-CD5","description":null,"displayColor":"#b925ff","liquidGroupId":"16","liquidClass":"waterV1"},"17":{"displayName":"LpGS-CD5","description":null,"displayColor":"#ffd600","liquidGroupId":"17","liquidClass":"waterV1"},"18":{"displayName":"LVP_MINOS_LINEAR_BACKBONE","description":null,"displayColor":"#b925ffff","liquidGroupId":"18","liquidClass":"waterV1"},"19":{"displayName":"DpnI","displayColor":"#ff9900","liquidClass":"glycerol50V1","description":null,"liquidGroupId":"19"},"20":{"displayName":"rCutsmart 10X","displayColor":"#50d5ff","liquidClass":"waterV1","description":null,"liquidGroupId":"20"},"21":{"displayName":"F1","displayColor":"#ff80f5","liquidClass":"waterV1","description":null,"liquidGroupId":"21"},"22":{"displayName":"R1","displayColor":"#7eff42","liquidClass":"waterV1","description":null,"liquidGroupId":"22"},"23":{"displayName":"F2","displayColor":"#ff4f4f","liquidClass":"waterV1","description":null,"liquidGroupId":"23"},"24":{"displayName":"R2","displayColor":"#b925ff","liquidClass":"waterV1","description":null,"liquidGroupId":"24"}},"ingredLocations":{"a8e358d7-441e-424e-a17d-2696f9d818ae:opentrons/opentrons_96_wellplate_200ul_pcr_full_skirt/2":{},"e12464ad-5c4e-4bd8-9585-e2001d8068f7:opentrons/armadillo_96_wellplate_200ul_pcr_full_skirt/3":{"A12":{"2":{"volume":125}},"B12":{"2":{"volume":125}},"C12":{"2":{"volume":125}},"D12":{"2":{"volume":125}},"H12":{"19":{"volume":10}},"G12":{"20":{"volume":50}},"A11":{"21":{"volume":20}},"B11":{"22":{"volume":20}},"C11":{"23":{"volume":20}},"D11":{"24":{"volume":20}},"H11":{"5":{"volume":10}},"A10":{"6":{"volume":200}},"B10":{"6":{"volume":200}},"C10":{"6":{"volume":200}},"D10":{"6":{"volume":200}},"E10":{"6":{"volume":200}},"F10":{"6":{"volume":200}},"G10":{"6":{"volume":200}},"H10":{"6":{"volume":200}}},"1a5fd57e-53b2-42ee-9803-80f9ea6be0cd:opentrons/opentrons_flex_96_filtertiprack_50ul/1":{},"d267ddb1-a4ed-4278-9a0b-3c076d137ece:opentrons/opentrons_flex_96_filtertiprack_50ul/1":{}},"savedStepForms":{"__INITIAL_DECK_SETUP_STEP__":{"labwareLocationUpdate":{"c4037252-d31d-48da-bc54-bf3427ca692d:opentrons/opentrons_flex_96_filtertiprack_50ul/1":"A2","a8e358d7-441e-424e-a17d-2696f9d818ae:opentrons/opentrons_96_wellplate_200ul_pcr_full_skirt/2":"7c5b741b-c2ac-4c8e-9f34-f51291c0301b:thermocyclerModuleType","9058e65f-a2d8-43dc-949b-5f08562afeb6:opentrons/opentrons_96_well_aluminum_block/1":"d0f9135f-5d38-4678-baa5-3c6c9ebafd66:temperatureModuleType","e12464ad-5c4e-4bd8-9585-e2001d8068f7:opentrons/armadillo_96_wellplate_200ul_pcr_full_skirt/3":"9058e65f-a2d8-43dc-949b-5f08562afeb6:opentrons/opentrons_96_well_aluminum_block/1","1a5fd57e-53b2-42ee-9803-80f9ea6be0cd:opentrons/opentrons_flex_96_filtertiprack_50ul/1":"A3","d267ddb1-a4ed-4278-9a0b-3c076d137ece:opentrons/opentrons_flex_96_filtertiprack_50ul/1":"B2"},"moduleLocationUpdate":{"7c5b741b-c2ac-4c8e-9f34-f51291c0301b:thermocyclerModuleType":"B1","ab876e4b-79ff-4c3e-8f5f-220e5289df0f:heaterShakerModuleType":"D1","d0f9135f-5d38-4678-baa5-3c6c9ebafd66:temperatureModuleType":"C1"},"pipetteLocationUpdate":{"63555313-4253-4347-be9c-8b6e64189bb7":"right","8e36439e-b289-4759-8202-396adc7c9436":"left"},"trashBinLocationUpdate":{},"wasteChuteLocationUpdate":{"0c55a7dd-a000-4ab5-ba2f-6e318b4d58c3:wasteChute":"cutoutD3"},"stagingAreaLocationUpdate":{"b5e29851-8f38-4701-a8c8-37bd3e2de6a0:stagingArea":"cutoutD3"},"gripperLocationUpdate":{"05d06909-404b-47dd-b2bd-40a6fe66a6be:gripper":"mounted"},"stepType":"manualIntervention","id":"__INITIAL_DECK_SETUP_STEP__"},"6b6b5be8-7602-400b-b3b6-6b884d86227d":{"blockIsActive":false,"blockIsActiveHold":true,"blockTargetTemp":null,"blockTargetTempHold":"10","lidIsActive":false,"lidIsActiveHold":true,"lidOpen":false,"lidOpenHold":true,"lidTargetTemp":null,"lidTargetTempHold":"37","moduleId":"7c5b741b-c2ac-4c8e-9f34-f51291c0301b:thermocyclerModuleType","orderedProfileItems":["2b1eabcf-3368-4b00-93e9-199420b95037","1d50b86f-5f8c-4537-808b-f049f901bf1b","7dcce4b4-ccad-4935-99e0-211844372afb"],"profileItemsById":{"2b1eabcf-3368-4b00-93e9-199420b95037":{"durationMinutes":"00","durationSeconds":"30","id":"2b1eabcf-3368-4b00-93e9-199420b95037","temperature":"98","title":"denature","type":"profileStep"},"1d50b86f-5f8c-4537-808b-f049f901bf1b":{"id":"1d50b86f-5f8c-4537-808b-f049f901bf1b","title":"","steps":[{"durationMinutes":"00","durationSeconds":"10","id":"2ed9985d-1920-4034-a608-28b2d62e38e8","temperature":"98","title":"d","type":"profileStep"},{"durationMinutes":"00","durationSeconds":"10","id":"e66646c5-9443-487c-a472-e07ac50fa557","temperature":"68","title":"a","type":"profileStep"},{"durationMinutes":"01","durationSeconds":"10","id":"832cd7a7-3562-45da-862d-e4120d496036","temperature":"72","title":"e","type":"profileStep"}],"type":"profileCycle","repetitions":"25"},"7dcce4b4-ccad-4935-99e0-211844372afb":{"durationMinutes":"02","durationSeconds":"00","id":"7dcce4b4-ccad-4935-99e0-211844372afb","temperature":"72","title":"final ext","type":"profileStep"}},"profileTargetLidTemp":"110","profileVolume":"50","thermocyclerFormType":"thermocyclerProfile","id":"6b6b5be8-7602-400b-b3b6-6b884d86227d","stepType":"thermocycler","stepName":"Q5 Tm 68","stepDetails":""},"22e85f9f-5dfe-4324-988f-4426ac635b57":{"moduleId":"d0f9135f-5d38-4678-baa5-3c6c9ebafd66:temperatureModuleType","setTemperature":"true","targetTemperature":"10","id":"22e85f9f-5dfe-4324-988f-4426ac635b57","stepType":"temperature","stepName":"temperature module state","stepDetails":"","stepNumber":0},"9130e663-8749-4ae7-8d43-092d2f293afe":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":true,"aspirate_delay_seconds":"1","aspirate_flowRate":"50","aspirate_labware":"e12464ad-5c4e-4bd8-9585-e2001d8068f7:opentrons/armadillo_96_wellplate_200ul_pcr_full_skirt/3","aspirate_mix_checkbox":false,"aspirate_mix_times":"1","aspirate_mix_volume":"50","aspirate_mmFromBottom":2,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"4","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"4","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A12"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":true,"blowout_flowRate":"25","blowout_location":"0c55a7dd-a000-4ab5-ba2f-6e318b4d58c3:wasteChute","changeTip":"once","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":true,"dispense_delay_seconds":"0.5","dispense_flowRate":"25","dispense_labware":"a8e358d7-441e-424e-a17d-2696f9d818ae:opentrons/opentrons_96_wellplate_200ul_pcr_full_skirt/2","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":2,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"4","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"4","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["C1","D1"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"0c55a7dd-a000-4ab5-ba2f-6e318b4d58c3:wasteChute","liquidClassesSupported":true,"liquidClass":"glycerol50V1","nozzles":null,"path":"multiDispense","pipette":"63555313-4253-4347-be9c-8b6e64189bb7","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":"3.9","tipRack":"opentrons/opentrons_flex_96_filtertiprack_50ul/1","volume":"25","stepType":"moveLiquid","stepName":"Q5 distribute: Tm68","stepDetails":"","id":"9130e663-8749-4ae7-8d43-092d2f293afe","dispense_touchTip_mmfromTop":null},"25396779-4b61-4266-91db-7e71661c5061":{"aspirate_airGap_checkbox":true,"aspirate_airGap_volume":"0.1","aspirate_delay_checkbox":true,"aspirate_delay_seconds":"0.2","aspirate_flowRate":"28.8","aspirate_labware":"a8e358d7-441e-424e-a17d-2696f9d818ae:opentrons/opentrons_96_wellplate_200ul_pcr_full_skirt/2","aspirate_mix_checkbox":false,"aspirate_mix_times":"1","aspirate_mix_volume":"50","aspirate_mmFromBottom":2,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"50","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"100","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["C1","D1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"50","blowout_location":"dest_well","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":true,"dispense_airGap_volume":"0.1","dispense_delay_checkbox":true,"dispense_delay_seconds":"0.2","dispense_flowRate":"50","dispense_labware":"e12464ad-5c4e-4bd8-9585-e2001d8068f7:opentrons/armadillo_96_wellplate_200ul_pcr_full_skirt/3","dispense_mix_checkbox":false,"dispense_mix_times":"1","dispense_mix_volume":"50","dispense_mmFromBottom":2,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"50","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"100","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["C1","D1"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"0c55a7dd-a000-4ab5-ba2f-6e318b4d58c3:wasteChute","liquidClassesSupported":true,"liquidClass":"waterV1","nozzles":null,"path":"single","pipette":"63555313-4253-4347-be9c-8b6e64189bb7","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":"2","tipRack":"opentrons/opentrons_flex_96_filtertiprack_50ul/1","volume":"55","id":"25396779-4b61-4266-91db-7e71661c5061","stepType":"moveLiquid","stepName":"Move PCR to 10C block","stepDetails":"","stepNumber":0},"6adc5c02-a723-433d-8525-b32aa540b6df":{"id":"6adc5c02-a723-433d-8525-b32aa540b6df","stepType":"moveLiquid","stepName":"Transfer F1","stepDetails":"","stepNumber":0,"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":null,"aspirate_delay_checkbox":true,"aspirate_delay_seconds":"0.2","aspirate_flowRate":"25.3","aspirate_labware":"e12464ad-5c4e-4bd8-9585-e2001d8068f7:opentrons/armadillo_96_wellplate_200ul_pcr_full_skirt/3","aspirate_mix_checkbox":false,"aspirate_mix_times":"1","aspirate_mix_volume":"50","aspirate_mmFromBottom":2,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"50","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"100","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["C11"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"50","blowout_location":"0c55a7dd-a000-4ab5-ba2f-6e318b4d58c3:wasteChute","changeTip":"once","conditioning_checkbox":true,"conditioning_volume":"5","dispense_airGap_checkbox":true,"dispense_airGap_volume":"0.1","dispense_delay_checkbox":true,"dispense_delay_seconds":"0.2","dispense_flowRate":"43","dispense_labware":"a8e358d7-441e-424e-a17d-2696f9d818ae:opentrons/opentrons_96_wellplate_200ul_pcr_full_skirt/2","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":2,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"50","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"100","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["C1","D1"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"5","dropTip_location":"0c55a7dd-a000-4ab5-ba2f-6e318b4d58c3:wasteChute","liquidClassesSupported":true,"liquidClass":"waterV1","nozzles":null,"path":"multiDispense","pipette":"63555313-4253-4347-be9c-8b6e64189bb7","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":"7","tipRack":"opentrons/opentrons_flex_96_filtertiprack_50ul/1","volume":"2.5"},"15eeacba-785b-4129-8640-02e178e2e617":{"id":"15eeacba-785b-4129-8640-02e178e2e617","stepType":"moveLiquid","stepName":"Transfer R1","stepDetails":"","stepNumber":0,"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":null,"aspirate_delay_checkbox":true,"aspirate_delay_seconds":"0.2","aspirate_flowRate":"25.3","aspirate_labware":"e12464ad-5c4e-4bd8-9585-e2001d8068f7:opentrons/armadillo_96_wellplate_200ul_pcr_full_skirt/3","aspirate_mix_checkbox":false,"aspirate_mix_times":"1","aspirate_mix_volume":"50","aspirate_mmFromBottom":2,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"50","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"100","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["D11"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"50","blowout_location":"0c55a7dd-a000-4ab5-ba2f-6e318b4d58c3:wasteChute","changeTip":"once","conditioning_checkbox":true,"conditioning_volume":"5","dispense_airGap_checkbox":true,"dispense_airGap_volume":"0.1","dispense_delay_checkbox":true,"dispense_delay_seconds":"0.2","dispense_flowRate":"43","dispense_labware":"a8e358d7-441e-424e-a17d-2696f9d818ae:opentrons/opentrons_96_wellplate_200ul_pcr_full_skirt/2","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":2,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"50","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"100","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["C1","D1"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"5","dropTip_location":"0c55a7dd-a000-4ab5-ba2f-6e318b4d58c3:wasteChute","liquidClassesSupported":true,"liquidClass":"waterV1","nozzles":null,"path":"multiDispense","pipette":"63555313-4253-4347-be9c-8b6e64189bb7","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":"7","tipRack":"opentrons/opentrons_flex_96_filtertiprack_50ul/1","volume":"2.5"},"c899893d-9a28-4268-9b6c-209ceec7484d":{"moduleId":"d0f9135f-5d38-4678-baa5-3c6c9ebafd66:temperatureModuleType","setTemperature":"true","targetTemperature":"10","id":"c899893d-9a28-4268-9b6c-209ceec7484d","stepType":"temperature","stepName":"temperature module state","stepDetails":"","stepNumber":0},"1e5d6e91-368b-4e6f-bde4-72e947aba73d":{"blockIsActive":true,"blockIsActiveHold":false,"blockTargetTemp":"10","blockTargetTempHold":null,"lidIsActive":false,"lidIsActiveHold":false,"lidOpen":true,"lidOpenHold":null,"lidTargetTemp":"","lidTargetTempHold":null,"moduleId":"7c5b741b-c2ac-4c8e-9f34-f51291c0301b:thermocyclerModuleType","orderedProfileItems":[],"profileItemsById":{},"profileTargetLidTemp":null,"profileVolume":null,"thermocyclerFormType":"thermocyclerState","id":"1e5d6e91-368b-4e6f-bde4-72e947aba73d","stepType":"thermocycler","stepName":"thermocycler","stepDetails":""},"2c06beaa-eb2c-4176-966d-884b676e90ee":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":true,"aspirate_delay_seconds":"1","aspirate_flowRate":"50","aspirate_labware":"e12464ad-5c4e-4bd8-9585-e2001d8068f7:opentrons/armadillo_96_wellplate_200ul_pcr_full_skirt/3","aspirate_mix_checkbox":false,"aspirate_mix_times":"1","aspirate_mix_volume":"50","aspirate_mmFromBottom":2,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"4","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"4","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A12"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":true,"blowout_flowRate":"25","blowout_location":"0c55a7dd-a000-4ab5-ba2f-6e318b4d58c3:wasteChute","changeTip":"once","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":true,"dispense_delay_seconds":"0.5","dispense_flowRate":"25","dispense_labware":"a8e358d7-441e-424e-a17d-2696f9d818ae:opentrons/opentrons_96_wellplate_200ul_pcr_full_skirt/2","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":2,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"4","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"4","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A1","B1"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"0c55a7dd-a000-4ab5-ba2f-6e318b4d58c3:wasteChute","liquidClassesSupported":true,"liquidClass":"glycerol50V1","nozzles":null,"path":"multiDispense","pipette":"63555313-4253-4347-be9c-8b6e64189bb7","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":"3.9","tipRack":"opentrons/opentrons_flex_96_filtertiprack_50ul/1","volume":"25","stepType":"moveLiquid","stepName":"Q5 distribute: Tm67","stepDetails":"","id":"2c06beaa-eb2c-4176-966d-884b676e90ee","dispense_touchTip_mmfromTop":null},"616bfbd0-20c6-46fc-8818-d1d1f0e638a4":{"id":"616bfbd0-20c6-46fc-8818-d1d1f0e638a4","stepType":"moveLiquid","stepName":"Transfer F1","stepDetails":"","stepNumber":0,"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":null,"aspirate_delay_checkbox":true,"aspirate_delay_seconds":"0.2","aspirate_flowRate":"25.3","aspirate_labware":"e12464ad-5c4e-4bd8-9585-e2001d8068f7:opentrons/armadillo_96_wellplate_200ul_pcr_full_skirt/3","aspirate_mix_checkbox":false,"aspirate_mix_times":"1","aspirate_mix_volume":"50","aspirate_mmFromBottom":2,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"50","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"100","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A11"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"50","blowout_location":"0c55a7dd-a000-4ab5-ba2f-6e318b4d58c3:wasteChute","changeTip":"once","conditioning_checkbox":true,"conditioning_volume":"5","dispense_airGap_checkbox":true,"dispense_airGap_volume":"0.1","dispense_delay_checkbox":true,"dispense_delay_seconds":"0.2","dispense_flowRate":"43","dispense_labware":"a8e358d7-441e-424e-a17d-2696f9d818ae:opentrons/opentrons_96_wellplate_200ul_pcr_full_skirt/2","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":2,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"50","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"100","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A1","B1"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"5","dropTip_location":"0c55a7dd-a000-4ab5-ba2f-6e318b4d58c3:wasteChute","liquidClassesSupported":true,"liquidClass":"waterV1","nozzles":null,"path":"multiDispense","pipette":"63555313-4253-4347-be9c-8b6e64189bb7","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":"7","tipRack":"opentrons/opentrons_flex_96_filtertiprack_50ul/1","volume":"2.5"},"2f169473-7063-4090-8147-8fa205353857":{"id":"2f169473-7063-4090-8147-8fa205353857","stepType":"moveLiquid","stepName":"Transfer R1","stepDetails":"","stepNumber":0,"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":null,"aspirate_delay_checkbox":true,"aspirate_delay_seconds":"0.2","aspirate_flowRate":"25.3","aspirate_labware":"e12464ad-5c4e-4bd8-9585-e2001d8068f7:opentrons/armadillo_96_wellplate_200ul_pcr_full_skirt/3","aspirate_mix_checkbox":false,"aspirate_mix_times":"1","aspirate_mix_volume":"50","aspirate_mmFromBottom":2,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"50","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"100","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["B11"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"50","blowout_location":"0c55a7dd-a000-4ab5-ba2f-6e318b4d58c3:wasteChute","changeTip":"once","conditioning_checkbox":true,"conditioning_volume":"5","dispense_airGap_checkbox":true,"dispense_airGap_volume":"0.1","dispense_delay_checkbox":true,"dispense_delay_seconds":"0.2","dispense_flowRate":"43","dispense_labware":"a8e358d7-441e-424e-a17d-2696f9d818ae:opentrons/opentrons_96_wellplate_200ul_pcr_full_skirt/2","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":2,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"50","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"100","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A1","B1"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"5","dropTip_location":"0c55a7dd-a000-4ab5-ba2f-6e318b4d58c3:wasteChute","liquidClassesSupported":true,"liquidClass":"waterV1","nozzles":null,"path":"multiDispense","pipette":"63555313-4253-4347-be9c-8b6e64189bb7","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":"7","tipRack":"opentrons/opentrons_flex_96_filtertiprack_50ul/1","volume":"2.5"},"6bfcd2ea-e9c2-4bc3-9650-430aed17dca4":{"blockIsActive":false,"blockIsActiveHold":true,"blockTargetTemp":null,"blockTargetTempHold":"10","lidIsActive":false,"lidIsActiveHold":true,"lidOpen":false,"lidOpenHold":true,"lidTargetTemp":null,"lidTargetTempHold":"37","moduleId":"7c5b741b-c2ac-4c8e-9f34-f51291c0301b:thermocyclerModuleType","orderedProfileItems":["2b1eabcf-3368-4b00-93e9-199420b95037","1d50b86f-5f8c-4537-808b-f049f901bf1b","7dcce4b4-ccad-4935-99e0-211844372afb"],"profileItemsById":{"2b1eabcf-3368-4b00-93e9-199420b95037":{"durationMinutes":"00","durationSeconds":"30","id":"2b1eabcf-3368-4b00-93e9-199420b95037","temperature":"98","title":"denature","type":"profileStep"},"1d50b86f-5f8c-4537-808b-f049f901bf1b":{"id":"1d50b86f-5f8c-4537-808b-f049f901bf1b","title":"","steps":[{"durationMinutes":"00","durationSeconds":"10","id":"2ed9985d-1920-4034-a608-28b2d62e38e8","temperature":"98","title":"d","type":"profileStep"},{"durationMinutes":"00","durationSeconds":"10","id":"e66646c5-9443-487c-a472-e07ac50fa557","temperature":"65","title":"a","type":"profileStep"},{"durationMinutes":"01","durationSeconds":"10","id":"832cd7a7-3562-45da-862d-e4120d496036","temperature":"72","title":"e","type":"profileStep"}],"type":"profileCycle","repetitions":"25"},"7dcce4b4-ccad-4935-99e0-211844372afb":{"durationMinutes":"02","durationSeconds":"00","id":"7dcce4b4-ccad-4935-99e0-211844372afb","temperature":"72","title":"final ext","type":"profileStep"}},"profileTargetLidTemp":"110","profileVolume":"50","thermocyclerFormType":"thermocyclerProfile","id":"6bfcd2ea-e9c2-4bc3-9650-430aed17dca4","stepType":"thermocycler","stepName":"Q5 Tm 65","stepDetails":""},"92919ef7-2411-4bc9-9f37-96b33666f8bb":{"aspirate_airGap_checkbox":true,"aspirate_airGap_volume":"0.1","aspirate_delay_checkbox":true,"aspirate_delay_seconds":"0.2","aspirate_flowRate":"28.8","aspirate_labware":"a8e358d7-441e-424e-a17d-2696f9d818ae:opentrons/opentrons_96_wellplate_200ul_pcr_full_skirt/2","aspirate_mix_checkbox":false,"aspirate_mix_times":"1","aspirate_mix_volume":"50","aspirate_mmFromBottom":2,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"50","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"100","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A1","B1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"50","blowout_location":"dest_well","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":true,"dispense_airGap_volume":"0.1","dispense_delay_checkbox":true,"dispense_delay_seconds":"0.2","dispense_flowRate":"50","dispense_labware":"e12464ad-5c4e-4bd8-9585-e2001d8068f7:opentrons/armadillo_96_wellplate_200ul_pcr_full_skirt/3","dispense_mix_checkbox":false,"dispense_mix_times":"1","dispense_mix_volume":"50","dispense_mmFromBottom":2,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"50","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"100","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A1","B1"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"0c55a7dd-a000-4ab5-ba2f-6e318b4d58c3:wasteChute","liquidClassesSupported":true,"liquidClass":"waterV1","nozzles":null,"path":"single","pipette":"63555313-4253-4347-be9c-8b6e64189bb7","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":"2","tipRack":"opentrons/opentrons_flex_96_filtertiprack_50ul/1","volume":"55","id":"92919ef7-2411-4bc9-9f37-96b33666f8bb","stepType":"moveLiquid","stepName":"Move PCR to 10C block","stepDetails":"","stepNumber":0},"6705aa27-ac02-4787-8de7-e806dde4f05f":{"id":"6705aa27-ac02-4787-8de7-e806dde4f05f","stepType":"moveLiquid","stepName":"Transfer H2O","stepDetails":"","stepNumber":0,"aspirate_airGap_checkbox":true,"aspirate_airGap_volume":"0.1","aspirate_delay_checkbox":true,"aspirate_delay_seconds":"0.2","aspirate_flowRate":"26.4","aspirate_labware":"e12464ad-5c4e-4bd8-9585-e2001d8068f7:opentrons/armadillo_96_wellplate_200ul_pcr_full_skirt/3","aspirate_mix_checkbox":false,"aspirate_mix_times":"1","aspirate_mix_volume":"50","aspirate_mmFromBottom":2,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"50","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"100","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A10"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"50","blowout_location":"dest_well","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":true,"dispense_airGap_volume":"0.1","dispense_delay_checkbox":true,"dispense_delay_seconds":"0.2","dispense_flowRate":"50","dispense_labware":"a8e358d7-441e-424e-a17d-2696f9d818ae:opentrons/opentrons_96_wellplate_200ul_pcr_full_skirt/2","dispense_mix_checkbox":true,"dispense_mix_times":"5","dispense_mix_volume":"25","dispense_mmFromBottom":2,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"50","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"100","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A1","B1"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"0c55a7dd-a000-4ab5-ba2f-6e318b4d58c3:wasteChute","liquidClassesSupported":true,"liquidClass":"waterV1","nozzles":null,"path":"single","pipette":"63555313-4253-4347-be9c-8b6e64189bb7","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":"2","tipRack":"opentrons/opentrons_flex_96_filtertiprack_50ul/1","volume":"19"},"1d7e711f-88e6-42ce-85cd-45718dc8e698":{"id":"1d7e711f-88e6-42ce-85cd-45718dc8e698","stepType":"moveLiquid","stepName":"Transfer H2O","stepDetails":"","stepNumber":0,"aspirate_airGap_checkbox":true,"aspirate_airGap_volume":"0.1","aspirate_delay_checkbox":true,"aspirate_delay_seconds":"0.2","aspirate_flowRate":"26.4","aspirate_labware":"e12464ad-5c4e-4bd8-9585-e2001d8068f7:opentrons/armadillo_96_wellplate_200ul_pcr_full_skirt/3","aspirate_mix_checkbox":false,"aspirate_mix_times":"1","aspirate_mix_volume":"50","aspirate_mmFromBottom":2,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"50","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"100","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["B10"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"50","blowout_location":"dest_well","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":true,"dispense_airGap_volume":"0.1","dispense_delay_checkbox":true,"dispense_delay_seconds":"0.2","dispense_flowRate":"50","dispense_labware":"a8e358d7-441e-424e-a17d-2696f9d818ae:opentrons/opentrons_96_wellplate_200ul_pcr_full_skirt/2","dispense_mix_checkbox":true,"dispense_mix_times":"5","dispense_mix_volume":"25","dispense_mmFromBottom":2,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"50","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"100","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["C1","D1"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"0c55a7dd-a000-4ab5-ba2f-6e318b4d58c3:wasteChute","liquidClassesSupported":true,"liquidClass":"waterV1","nozzles":null,"path":"single","pipette":"63555313-4253-4347-be9c-8b6e64189bb7","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":"2","tipRack":"opentrons/opentrons_flex_96_filtertiprack_50ul/1","volume":"19"},"c6a27936-66a4-4fb7-bc6f-00b1feb06884":{"id":"c6a27936-66a4-4fb7-bc6f-00b1feb06884","stepType":"moveLiquid","stepName":"Transfer template","stepDetails":"","stepNumber":0,"aspirate_airGap_checkbox":true,"aspirate_airGap_volume":"0.1","aspirate_delay_checkbox":true,"aspirate_delay_seconds":"0.2","aspirate_flowRate":"33","aspirate_labware":"e12464ad-5c4e-4bd8-9585-e2001d8068f7:opentrons/armadillo_96_wellplate_200ul_pcr_full_skirt/3","aspirate_mix_checkbox":false,"aspirate_mix_times":"1","aspirate_mix_volume":"50","aspirate_mmFromBottom":2,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"50","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"100","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["H11"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"50","blowout_location":"dest_well","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":true,"dispense_airGap_volume":"0.1","dispense_delay_checkbox":true,"dispense_delay_seconds":"0.2","dispense_flowRate":"33","dispense_labware":"a8e358d7-441e-424e-a17d-2696f9d818ae:opentrons/opentrons_96_wellplate_200ul_pcr_full_skirt/2","dispense_mix_checkbox":false,"dispense_mix_times":"1","dispense_mix_volume":"50","dispense_mmFromBottom":2,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"50","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"100","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A1","B1"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"0c55a7dd-a000-4ab5-ba2f-6e318b4d58c3:wasteChute","liquidClassesSupported":true,"liquidClass":"waterV1","nozzles":null,"path":"single","pipette":"63555313-4253-4347-be9c-8b6e64189bb7","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":"7","tipRack":"opentrons/opentrons_flex_96_filtertiprack_50ul/1","volume":"1"},"f7b1426b-4e38-4c89-bf3c-5793f4f6af9b":{"id":"f7b1426b-4e38-4c89-bf3c-5793f4f6af9b","stepType":"moveLiquid","stepName":"Transfer template","stepDetails":"","stepNumber":0,"aspirate_airGap_checkbox":true,"aspirate_airGap_volume":"0.1","aspirate_delay_checkbox":true,"aspirate_delay_seconds":"0.2","aspirate_flowRate":"33","aspirate_labware":"e12464ad-5c4e-4bd8-9585-e2001d8068f7:opentrons/armadillo_96_wellplate_200ul_pcr_full_skirt/3","aspirate_mix_checkbox":false,"aspirate_mix_times":"1","aspirate_mix_volume":"50","aspirate_mmFromBottom":2,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"50","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"100","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["H11"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"50","blowout_location":"dest_well","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":true,"dispense_airGap_volume":"0.1","dispense_delay_checkbox":true,"dispense_delay_seconds":"0.2","dispense_flowRate":"33","dispense_labware":"a8e358d7-441e-424e-a17d-2696f9d818ae:opentrons/opentrons_96_wellplate_200ul_pcr_full_skirt/2","dispense_mix_checkbox":false,"dispense_mix_times":"1","dispense_mix_volume":"50","dispense_mmFromBottom":2,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"50","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"100","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["C1","D1"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"0c55a7dd-a000-4ab5-ba2f-6e318b4d58c3:wasteChute","liquidClassesSupported":true,"liquidClass":"waterV1","nozzles":null,"path":"single","pipette":"63555313-4253-4347-be9c-8b6e64189bb7","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":"7","tipRack":"opentrons/opentrons_flex_96_filtertiprack_50ul/1","volume":"1"},"680fd73b-48b1-43b6-a586-747ce57342bd":{"id":"680fd73b-48b1-43b6-a586-747ce57342bd","stepType":"moveLiquid","stepName":"Transfer DpnI","stepDetails":"","stepNumber":0,"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":true,"aspirate_delay_seconds":"1","aspirate_flowRate":"7.3","aspirate_labware":"e12464ad-5c4e-4bd8-9585-e2001d8068f7:opentrons/armadillo_96_wellplate_200ul_pcr_full_skirt/3","aspirate_mix_checkbox":false,"aspirate_mix_times":"1","aspirate_mix_volume":"50","aspirate_mmFromBottom":2,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"4","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"4","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["H12"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"25","blowout_location":"dest_well","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":true,"dispense_delay_seconds":"0.5","dispense_flowRate":"25","dispense_labware":"e12464ad-5c4e-4bd8-9585-e2001d8068f7:opentrons/armadillo_96_wellplate_200ul_pcr_full_skirt/3","dispense_mix_checkbox":false,"dispense_mix_times":"1","dispense_mix_volume":"50","dispense_mmFromBottom":2,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"4","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"4","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A1","B1","C1","D1"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"0c55a7dd-a000-4ab5-ba2f-6e318b4d58c3:wasteChute","liquidClassesSupported":true,"liquidClass":"glycerol50V1","nozzles":null,"path":"single","pipette":"63555313-4253-4347-be9c-8b6e64189bb7","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":"11.7","tipRack":"opentrons/opentrons_flex_96_filtertiprack_50ul/1","volume":"2"},"f7136876-6d56-4899-b370-8384affb5eb9":{"id":"f7136876-6d56-4899-b370-8384affb5eb9","stepType":"moveLiquid","stepName":"transfer","stepDetails":"","stepNumber":0,"aspirate_airGap_checkbox":true,"aspirate_airGap_volume":"0.1","aspirate_delay_checkbox":true,"aspirate_delay_seconds":"0.2","aspirate_flowRate":"24","aspirate_labware":"e12464ad-5c4e-4bd8-9585-e2001d8068f7:opentrons/armadillo_96_wellplate_200ul_pcr_full_skirt/3","aspirate_mix_checkbox":false,"aspirate_mix_times":"1","aspirate_mix_volume":"50","aspirate_mmFromBottom":2,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"50","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"100","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["G12"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"50","blowout_location":"dest_well","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":true,"dispense_airGap_volume":"0.1","dispense_delay_checkbox":true,"dispense_delay_seconds":"0.2","dispense_flowRate":"50","dispense_labware":"e12464ad-5c4e-4bd8-9585-e2001d8068f7:opentrons/armadillo_96_wellplate_200ul_pcr_full_skirt/3","dispense_mix_checkbox":false,"dispense_mix_times":"1","dispense_mix_volume":"50","dispense_mmFromBottom":2,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"50","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"100","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A1","B1","C1","D1"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"0c55a7dd-a000-4ab5-ba2f-6e318b4d58c3:wasteChute","liquidClassesSupported":true,"liquidClass":"waterV1","nozzles":null,"path":"single","pipette":"63555313-4253-4347-be9c-8b6e64189bb7","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":"2","tipRack":"opentrons/opentrons_flex_96_filtertiprack_50ul/1","volume":"10"},"d5c9baff-d0b3-42bb-b974-f3e2371b092e":{"id":"d5c9baff-d0b3-42bb-b974-f3e2371b092e","stepType":"moveLiquid","stepName":"Transfer H2O","stepDetails":"","stepNumber":0,"aspirate_airGap_checkbox":true,"aspirate_airGap_volume":"0.1","aspirate_delay_checkbox":true,"aspirate_delay_seconds":"0.2","aspirate_flowRate":"33.0","aspirate_labware":"e12464ad-5c4e-4bd8-9585-e2001d8068f7:opentrons/armadillo_96_wellplate_200ul_pcr_full_skirt/3","aspirate_mix_checkbox":false,"aspirate_mix_times":"1","aspirate_mix_volume":"50","aspirate_mmFromBottom":2,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"50","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"100","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["C10"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"50","blowout_location":"dest_well","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":true,"dispense_airGap_volume":"0.1","dispense_delay_checkbox":true,"dispense_delay_seconds":"0.2","dispense_flowRate":"50","dispense_labware":"e12464ad-5c4e-4bd8-9585-e2001d8068f7:opentrons/armadillo_96_wellplate_200ul_pcr_full_skirt/3","dispense_mix_checkbox":true,"dispense_mix_times":"5","dispense_mix_volume":"45","dispense_mmFromBottom":2,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"50","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"100","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A1","B1"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"0c55a7dd-a000-4ab5-ba2f-6e318b4d58c3:wasteChute","liquidClassesSupported":true,"liquidClass":"waterV1","nozzles":null,"path":"single","pipette":"63555313-4253-4347-be9c-8b6e64189bb7","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":"2","tipRack":"opentrons/opentrons_flex_96_filtertiprack_50ul/1","volume":"43"},"78801764-49ec-4814-b46f-94d9cfe9d50d":{"id":"78801764-49ec-4814-b46f-94d9cfe9d50d","stepType":"moveLiquid","stepName":"Transfer H2O","stepDetails":"","stepNumber":0,"aspirate_airGap_checkbox":true,"aspirate_airGap_volume":"0.1","aspirate_delay_checkbox":true,"aspirate_delay_seconds":"0.2","aspirate_flowRate":"33.0","aspirate_labware":"e12464ad-5c4e-4bd8-9585-e2001d8068f7:opentrons/armadillo_96_wellplate_200ul_pcr_full_skirt/3","aspirate_mix_checkbox":false,"aspirate_mix_times":"1","aspirate_mix_volume":"50","aspirate_mmFromBottom":2,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"50","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"100","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["D10"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"50","blowout_location":"dest_well","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":true,"dispense_airGap_volume":"0.1","dispense_delay_checkbox":true,"dispense_delay_seconds":"0.2","dispense_flowRate":"50","dispense_labware":"e12464ad-5c4e-4bd8-9585-e2001d8068f7:opentrons/armadillo_96_wellplate_200ul_pcr_full_skirt/3","dispense_mix_checkbox":true,"dispense_mix_times":"5","dispense_mix_volume":"45","dispense_mmFromBottom":2,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"50","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"100","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["C1","D1"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"0c55a7dd-a000-4ab5-ba2f-6e318b4d58c3:wasteChute","liquidClassesSupported":true,"liquidClass":"waterV1","nozzles":null,"path":"single","pipette":"63555313-4253-4347-be9c-8b6e64189bb7","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":"2","tipRack":"opentrons/opentrons_flex_96_filtertiprack_50ul/1","volume":"43"},"b7a266ec-b29f-41b5-aa51-6fb6dd4d3213":{"id":"b7a266ec-b29f-41b5-aa51-6fb6dd4d3213","stepType":"moveLiquid","stepName":"transfer","stepDetails":"","stepNumber":0,"aspirate_airGap_checkbox":true,"aspirate_airGap_volume":"0.1","aspirate_delay_checkbox":true,"aspirate_delay_seconds":"0.2","aspirate_flowRate":"31.3","aspirate_labware":"e12464ad-5c4e-4bd8-9585-e2001d8068f7:opentrons/armadillo_96_wellplate_200ul_pcr_full_skirt/3","aspirate_mix_checkbox":false,"aspirate_mix_times":"1","aspirate_mix_volume":"50","aspirate_mmFromBottom":2,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"50","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"100","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":-1,"aspirate_touchTip_speed":"30","aspirate_touchTip_mmFromEdge":"0.5","aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A1","B1","C1","D1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"50","blowout_location":"dest_well","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":"","dispense_airGap_checkbox":true,"dispense_airGap_volume":"0.1","dispense_delay_checkbox":true,"dispense_delay_seconds":"0.2","dispense_flowRate":"50","dispense_labware":"a8e358d7-441e-424e-a17d-2696f9d818ae:opentrons/opentrons_96_wellplate_200ul_pcr_full_skirt/2","dispense_mix_checkbox":false,"dispense_mix_times":"1","dispense_mix_volume":"50","dispense_mmFromBottom":2,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"50","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"100","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":-1,"dispense_touchTip_speed":"30","dispense_touchTip_mmFromEdge":"0.5","dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["E1","F1","G1","H1"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":"","dropTip_location":"0c55a7dd-a000-4ab5-ba2f-6e318b4d58c3:wasteChute","liquidClassesSupported":true,"liquidClass":"waterV1","nozzles":null,"path":"single","pipette":"63555313-4253-4347-be9c-8b6e64189bb7","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":"2","tipRack":"opentrons/opentrons_flex_96_filtertiprack_50ul/1","volume":"110"},"9e1dfa82-1e91-4c80-ab6b-0b7d38d0ea3b":{"id":"9e1dfa82-1e91-4c80-ab6b-0b7d38d0ea3b","stepType":"thermocycler","stepName":"Thermocycler: DpnI","stepDetails":"","stepNumber":0,"blockIsActive":false,"blockIsActiveHold":true,"blockTargetTemp":null,"blockTargetTempHold":"10","lidIsActive":false,"lidIsActiveHold":true,"lidOpen":false,"lidOpenHold":null,"lidTargetTemp":null,"lidTargetTempHold":"37","moduleId":"7c5b741b-c2ac-4c8e-9f34-f51291c0301b:thermocyclerModuleType","orderedProfileItems":["0d2410d2-4601-4882-9846-cd876f80a7d2","e677c6e2-9936-443d-8611-cef44feca878"],"profileItemsById":{"0d2410d2-4601-4882-9846-cd876f80a7d2":{"durationMinutes":"30","durationSeconds":"00","id":"0d2410d2-4601-4882-9846-cd876f80a7d2","temperature":"37","title":"DpnI","type":"profileStep"},"e677c6e2-9936-443d-8611-cef44feca878":{"durationMinutes":"20","durationSeconds":"00","id":"e677c6e2-9936-443d-8611-cef44feca878","temperature":"65","title":"heat denature","type":"profileStep"}},"profileTargetLidTemp":"110","profileVolume":"100","thermocyclerFormType":"thermocyclerProfile"}},"orderedStepIds":["22e85f9f-5dfe-4324-988f-4426ac635b57","c899893d-9a28-4268-9b6c-209ceec7484d","1e5d6e91-368b-4e6f-bde4-72e947aba73d","2c06beaa-eb2c-4176-966d-884b676e90ee","616bfbd0-20c6-46fc-8818-d1d1f0e638a4","c6a27936-66a4-4fb7-bc6f-00b1feb06884","2f169473-7063-4090-8147-8fa205353857","6705aa27-ac02-4787-8de7-e806dde4f05f","6bfcd2ea-e9c2-4bc3-9650-430aed17dca4","92919ef7-2411-4bc9-9f37-96b33666f8bb","9130e663-8749-4ae7-8d43-092d2f293afe","6adc5c02-a723-433d-8525-b32aa540b6df","f7b1426b-4e38-4c89-bf3c-5793f4f6af9b","15eeacba-785b-4129-8640-02e178e2e617","1d7e711f-88e6-42ce-85cd-45718dc8e698","6b6b5be8-7602-400b-b3b6-6b884d86227d","25396779-4b61-4266-91db-7e71661c5061","680fd73b-48b1-43b6-a586-747ce57342bd","f7136876-6d56-4899-b370-8384affb5eb9","d5c9baff-d0b3-42bb-b974-f3e2371b092e","78801764-49ec-4814-b46f-94d9cfe9d50d","b7a266ec-b29f-41b5-aa51-6fb6dd4d3213","9e1dfa82-1e91-4c80-ab6b-0b7d38d0ea3b"],"pipettes":{"63555313-4253-4347-be9c-8b6e64189bb7":{"pipetteName":"p50_single_flex"},"8e36439e-b289-4759-8202-396adc7c9436":{"pipetteName":"p50_multi_flex"}},"modules":{"7c5b741b-c2ac-4c8e-9f34-f51291c0301b:thermocyclerModuleType":{"model":"thermocyclerModuleV2"},"ab876e4b-79ff-4c3e-8f5f-220e5289df0f:heaterShakerModuleType":{"model":"heaterShakerModuleV1"},"d0f9135f-5d38-4678-baa5-3c6c9ebafd66:temperatureModuleType":{"model":"temperatureModuleV2"}},"labware":{"c4037252-d31d-48da-bc54-bf3427ca692d:opentrons/opentrons_flex_96_filtertiprack_50ul/1":{"displayName":"Opentrons Flex 96 Filter Tip Rack 50 µL","labwareDefURI":"opentrons/opentrons_flex_96_filtertiprack_50ul/1"},"a8e358d7-441e-424e-a17d-2696f9d818ae:opentrons/opentrons_96_wellplate_200ul_pcr_full_skirt/2":{"displayName":"Opentrons Tough 96 Well Plate 200 µL PCR Full Skirt (1)","labwareDefURI":"opentrons/opentrons_96_wellplate_200ul_pcr_full_skirt/2"},"9058e65f-a2d8-43dc-949b-5f08562afeb6:opentrons/opentrons_96_well_aluminum_block/1":{"displayName":"Opentrons 96 Well Aluminum Block","labwareDefURI":"opentrons/opentrons_96_well_aluminum_block/1"},"e12464ad-5c4e-4bd8-9585-e2001d8068f7:opentrons/armadillo_96_wellplate_200ul_pcr_full_skirt/3":{"displayName":"(Retired) Armadillo 96 Well Plate 200 µL PCR Full Skirt","labwareDefURI":"opentrons/armadillo_96_wellplate_200ul_pcr_full_skirt/3"},"1a5fd57e-53b2-42ee-9803-80f9ea6be0cd:opentrons/opentrons_flex_96_filtertiprack_50ul/1":{"displayName":"Opentrons Flex 96 Filter Tip Rack 50 µL (1)","labwareDefURI":"opentrons/opentrons_flex_96_filtertiprack_50ul/1"},"d267ddb1-a4ed-4278-9a0b-3c076d137ece:opentrons/opentrons_flex_96_filtertiprack_50ul/1":{"displayName":"Opentrons Flex 96 Filter Tip Rack 50 µL (2)","labwareDefURI":"opentrons/opentrons_flex_96_filtertiprack_50ul/1"}}}},"metadata":{"protocolName":"Q5 PCR (Tm65+Tm68) + DpnI","author":"Evan Tjeerdema - SIO","description":"PCR for HiFi assembly. PCR off sequence fragments & plasmid. 10C hold at the end. Oligos and DNA fragments held at RT. Q5 and DpnI held at 10C. ","created":1753768164600,"lastModified":1756522456470,"category":null,"subcategory":null,"tags":[],"source":"Protocol Designer"}}"""
