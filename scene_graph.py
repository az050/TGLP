# Re-implemented data from 3D Scene Graph dataset
# Converting data structure from graph to nested Python dictionary
# Original data is in .npz format
# Added new objects for evaluation tasks (e.g., CPU, GPU, mop, banana_peel, locker, etc.)
# Source with MIT License: https://github.com/StanfordVL/3DSceneGraph



ALLENSVILLE = {
    "name": "allensville",
    "rooms": {
        "bathroom_1": {
            "items": {
                "psu": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free"
                },
                "sink_1": {
                    "accessible": True,
                    "affordance": ["clean_mop"],
                    "state": "free"
                },
                "toilet_1": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free"
                },
                "plant_1": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free"
                },
                "mop": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "clean_mop", "mop_floor"],
                    "state": "clean"
                },
                "detergent": {                                   #detergent
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free"
                }
            },
            "neighbor": ["corridor_2"]
        },
        "bathroom_2": {
            "items": {
                "gpu": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free"
                },
                "sink_2": {
                    "accessible": True,
                    "affordance": ["clean_mop"],
                    "state": "free"
                },
                "toilet_2": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free"
                },
                "plant_2": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free"
                }
            },
            "neighbor": ["corridor_3"]
        },
        "bedroom_1": {
            "items": {
                "mainboard": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free"
                },
                "glass": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "place_on"],
                    "state": "free"
                },
                "bed_1": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free"
                },
                "shelf": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "open","close","load", "unload"],
                    "state": "closed, loaded",
                    "content": {
                        "book": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free"
                        }
                    }
                },
            },
            "neighbor": ["corridor_2"]
        },
        "bedroom_2": {
            "items": {
                "cpu": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free"
                },
                "rotting_apple": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "dispose"],
                    "state": "free"
                },
                "plate": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "place_on"],
                    "state": "free"
                },
                "bed_2": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free"
                },
                "lamp": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free"
                },
                "clothes": {                                         ##clothes
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free, not-clean"
                },
                "desk": {
                    "accessible": True,
                    "affordance": [],
                    "state": "free"
                }
            },
            "neighbor": ["corridor_3"]
        },
        "corridor_1": {
            "items": {},
            "neighbor": ["lobby", "corridor_3"]
        },
        "corridor_2": {
            "items": {
                "fridge_1": {
                    "accessible": True,
                    "affordance": ["open", "close"],
                    "state": "closed, power_off"
                },
                "fridge_2": {
                    "accessible": True,
                    "affordance": ["open", "close"],
                    "state": "closed, power_off"
                }
            },
            "neighbor": ["bathroom_1", "bedroom_1", "corridor_3"]
        },
        "corridor_3": {
            "items": {},
            "neighbor": ["corridor_1", "corridor_2", "bathroom_2", "bedroom_2", "kitchen", "living_room"]
        },
        "dining_room": {
            "items": {
                "ssd": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free"
                },
                "clock": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free"
                },
                "cola_can": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "dispose"],
                    "state": "free"
                },
                "chair_1": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free"
                },
                "chair_2": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free"
                },
                "dining_table": {
                    "accessible": True,
                    "affordance": [],
                    "state": "free"
                }
            },
            "neighbor": ["kitchen", "living_room"]
        },
        "kitchen": {
            "items": {
                "knife": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "place_on"],
                    "state": "free"
                },
                "fork": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "place_on"],
                    "state": "free"
                },
                "spoon": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "place_on"],
                    "state": "free"
                },
                "microwave": {
                    "accessible": True,
                    "affordance": ["open", "close", "turnon", "turnoff"],
                    "state": "closed, power_off"
                },
                "oven": {
                    "accessible": True,
                    "affordance": ["turnon", "turnoff","open","close",],
                    "state": "closed, power_off"
                },
                "rubbish_bin": {
                    "accessible": True,
                    "affordance": ["dispose"],
                    "state": "free"
                },
                "fridge_3": {
                    "accessible": True,
                    "affordance": ["open", "close"],
                    "state": "free"
                },
                "chair_3": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free"
                },
                "mug": {                                                  #mug
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free"
                },
                "coffee_machine": {
                    "accessible": True,
                    "affordance": ["turnon", "turnoff"],
                    "state": "power_off"
                },
                "wash_machine": {                                              #wash_machine
                    "accessible": True,
                    "affordance": ["open", "close", "turnon", "turnoff"],
                    "state": "closed, power_off"
                }
            },
            "neighbor": ["corridor_3", "dining_room"]
        },
        "living_room": {
            "items": {
                "bowl_2": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free"
                },
                "bowl_3": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free"
                },
                "robot_hub": {
                    "accessible": True,
                    "affordance": ["charge"],
                    "state": "free"
                },
                "chair_4": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free"
                },
                "chair_5": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free"
                },
                "couch": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free"
                }
            },
            "neighbor": ["corridor_3", "dining_room"]
        },
        "lobby": {
            "items": {
                "ram": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free"
                },
                "banana_peel": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "dispose"],
                    "state": "free"
                },
                "flower": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "place_on"],
                    "state": "free"
                },
                "locker": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "open","close","load", "unload"],
                    "state": "closed, loaded",
                    "content": {
                        "paper": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free"
                        }
                    }
                }
            },
            "neighbor": ["corridor_1"]
        }
    },
    "agent": {
        "position": "living_room",
        "state": "hand-free, battery-full"
    },
    "human": {
        "name": "Tom",
        "position": "bedroom_1",
        "state": "hand-free"
    },
}

KEMBLESVILLE = {
    "name": "kemblesville",
    "rooms": {
        "bathroom": {
            "items": {
                "sink_1": {
                    "accessible": True,
                    "affordance": ["clean_mop"],
                    "state": "free"
                },
                "toilet": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free"
                },
                "detergent": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free"
                },
                "mop": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "clean_mop", "mop_floor"],
                    "state": "clean"
                }
            },
            "neighbor": ["corridor_1", "closet_1"]
        },
        "closet_1": {
            "items": {
                "clothes": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free, not-clean"
                },
                "ssd": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free"
                }
            },
            "neighbor": ["bathroom", "bedroom_1"]
        },
        "closet_2": {
            "items": {
                "fridge_1": {
                    "accessible": True,
                    "affordance": ["open", "close"],
                    "state": "closed, power_off"
                },
                "fridge_2": {
                    "accessible": True,
                    "affordance": ["open", "close"],
                    "state": "closed, power_off"
                }
            },
            "neighbor": ["corridor_2", "kitchen"]
        },
        "corridor_1": {
            "items": {
                "gpu": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free"
                },
                "lamp": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free"
                }
            },
            "neighbor": ["bedroom_1", "bedroom_2", "bathroom", "living_room"]
        },
        "corridor_2": {
            "items": {},
            "neighbor": ["closet_2", "kitchen", "living_room"]
        },
        "bedroom_1": {
            "items": {
                "bed_1": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free"
                },
                "mainboard": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free"
                },
                "flower": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "place_on"],
                    "state": "free"
                },
                "locker": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "open","close", "load", "unload"],
                    "state": "closed, loaded",
                    "content": {
                        "paper": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free"
                        }
                    }
                }
            },
            "neighbor": ["corridor_1", "closet_1"]
        },
        "bedroom_2": {
            "items": {
                "bed_2": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free"
                },
                "cpu": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free"
                },
                "desk": {
                    "accessible": True,
                    "affordance": [],
                    "state": "free"
                },
                "shelf": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "open","close","load", "unload"],
                    "state": "closed, loaded",
                    "content": {
                        "book": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free"
                        }
                    }
                }
            },
            "neighbor": ["corridor_1"]
        },
        "kitchen": {
            "items": {
                "wash_machine": {
                    "accessible": True,
                    "affordance": ["open", "close", "turnon", "turnoff"],
                    "state": "closed, power_off"
                },
                "microwave": {
                    "accessible": True,
                    "affordance": ["open", "close", "turnon", "turnoff"],
                    "state": "closed, power_off"
                },
                "oven": {
                    "accessible": True,
                    "affordance": ["turnon", "turnoff","open","close"],
                    "state": "closed, power_off"
                },
                "sink_2": {
                    "accessible": True,
                    "affordance": ["clean_mop"],
                    "state": "free"
                },
                "fridge_3": {
                    "accessible": True,
                    "affordance": ["open", "close"],
                    "state": "closed, power_off"
                },
                "mug": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free"
                },
                "coffee_machine": {
                    "accessible": True,
                    "affordance": ["turnon", "turnoff"],
                    "state": "power_off"
                },
                "banana_peel": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "dispose"],
                    "state": "free"
                },
                "rotting_apple": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "dispose"],
                    "state": "free"
                },
                 "rubbish_bin": {
                    "accessible": True,
                    "affordance": ["dispose"],
                    "state": "free"
                },
                "plate": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "place_on"],
                    "state": "free"
                },
                "fork": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "place_on"],
                    "state": "free"
                },
                "knife": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "place_on"],
                    "state": "free"
                },
                "spoon": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "place_on"],
                    "state": "free"
                }
            },
            "neighbor": ["corridor_2", "closet_2"]
        },
        "living_room": {
            "items": {
                "tv": {
                    "accessible": True,
                    "affordance": ["turnon", "turnoff"],
                    "state": "free"
                },
                "couch": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free"
                },
                "ram": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free"
                },
                "psu": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free"
                },
                "cola_can": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "dispose"],
                    "state": "free"
                },
                "robot_hub": {
                    "accessible": True,
                    "affordance": ["charge"],
                    "state": "free"
                },
                "glass": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "place_on"],
                    "state": "free"
                },
                "dining_table": {
                    "accessible": True,
                    "affordance": [],
                    "state": "free"
                }
            },
            "neighbor": ["corridor_1", "corridor_2"]
        },
    },
    "agent": {
        "position": "living_room",
        "state": "hand-free, battery-full"
    },
    "human": {
        "name": "Tom",
        "position": "bedroom_1",
        "state": "hand-free"
    },
}

PABLO = {
    "name": "pablo",
    "rooms": {
        "bathroom": {
            "items": {
                "sink": {
                    "accessible": True,
                    "affordance": ["clean_mop"],
                    "state": "free"
                },
                "bottle": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free"
                },
                "toilet": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free"
                },
                "detergent": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free"
                },
                "mop": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "clean_mop", "mop_floor"],
                    "state": "clean"
                }
            },
            "neighbor": ["corridor"]
        },
        "bedroom": {
            "items": {
                "book_1": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free"
                },
                "vase": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free"
                },
                "chair": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free"
                },
                "bed": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free"
                },
                "clothes": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free, not-clean"
                },
                "mainboard": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free"
                },
                "gpu": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free"
                },
                "spoon": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "place_on"],
                    "state": "free"
                },
                "flower": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "place_on"],
                    "state": "free"
                },
                "locker": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "open","close","load", "unload"],
                    "state": "closed, loaded",
                    "content": {
                        "paper": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free"
                        }
                    }
                },
                "lamp": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free"
                }
            },
            "neighbor": ["living_room"]
        },
        "closet": {
            "items": {
                "psu": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free"
                },
                "fork": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "place_on"],
                    "state": "free"
                },
                "knife": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "place_on"],
                    "state": "free"
                },
                "glass": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "place_on"],
                    "state": "free"
                }
            },
            "neighbor": ["corridor"]
        },
        "corridor": {
            "items": {
                "wash_machine": {
                    "accessible": True,
                    "affordance": ["open", "close", "turnon", "turnoff"],
                    "state": "closed, power_off"
                },
                "ssd": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free"
                },
                "desk": {
                    "accessible": True,
                    "affordance": [],
                    "state": "free"
                }
            },
            "neighbor": ["bathroom", "closet", "living_room"]
        },
        "living_room": {
            "items": {
                "couch": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free"
                },
                "tv": {
                    "accessible": True,
                    "affordance": ["turnon", "turnoff"],
                    "state": "power_off"
                },
                "mug": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free"
                },
                "coffee_machine": {
                    "accessible": True,
                    "affordance": ["turnon", "turnoff"],
                    "state": "power_off"
                },
                "cpu": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free"
                },
                "ram": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free"
                },
                "cola_can": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "dispose"],
                    "state": "free"
                },
                "banana_peel": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "dispose"],
                    "state": "free"
                },
                "rotting_apple": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "dispose"],
                    "state": "free"
                },
                "rubbish_bin": {
                    "accessible": True,
                    "affordance": ["dispose"],
                    "state": "free"
                },
                "robot_hub": {
                    "accessible": True,
                    "affordance": ["charge"],
                    "state": "free"
                },
                "plate": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "place_on"],
                    "state": "free"
                },
                "dining_table": {
                    "accessible": True,
                    "affordance": [],
                    "state": "free"
                },
                "shelf": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "open","close","load", "unload"],
                    "state": "closed, loaded",
                    "content": {
                        "book_2": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free"
                        }
                    }
                }
            },
            "neighbor": ["bedroom", "corridor"]
        }
    },
    "agent": {
        "position": "bedroom",
        "state": "hand-free, battery-full"
    },
    "human": {
        "name": "Tom",
        "position": "bedroom",
        "state": "hand-free"
    },
}

PAROLE = {
    "name": "parole",
    "rooms": {
        "bathroom": {
            "items": {
                "psu": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free"
                },
                "sink": {
                    "accessible": True,
                    "affordance": ["clean_mop"],
                    "state": "free"
                },
                "toilet": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free"
                },
                "detergent": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free"
                },
                "locker": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "open","close","load", "unload"],
                    "state": "closed, loaded",
                    "content": {
                        "paper": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free"
                        }
                    }
                },
            },
            "neighbor": ["corridor_2"]
        },
        "bedroom": {
            "items": {
                "cpu": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free"
                },
                "rotting_apple": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "dispose"],
                    "state": "free"
                },
                "bed": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free"
                },
                "glass": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "place_on"],
                    "state": "free"
                },
                "lamp": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free"
                },
                "shelf": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "open","close","load", "unload"],
                    "state": "closed, loaded",
                    "content": {
                        "book": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free"
                        }
                    }
                },
                "clothes": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free, not-clean"
                },
                "desk": {
                    "accessible": True,
                    "affordance": [],
                    "state": "free"
                }
            },
            "neighbor": ["corridor_2"]
        },
        "dining_room": {
            "items": {
                "ram": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free"
                },
                "cola_can": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "dispose"],
                    "state": "free"
                },
                "chair_1": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free"
                },
                "chair_2": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free"
                },
                "dining_table": {
                    "accessible": True,
                    "affordance": [],
                    "state": "free"
                },
                "mug": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free"
                },
            },
            "neighbor": ["corridor_1", "living_room"]
        },
        "corridor_1": {
            "items": {
                "flower": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "place_on"],
                    "state": "free"
                },
                "ssd": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free"
                },
                "mop": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "clean_mop", "mop_floor"],
                    "state": "clean"
                },
            },
            "neighbor": ["corridor_2", "dining_room", "kitchen"]
        },
        "corridor_2": {
            "items": {
                "gpu": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free"
                },
                "banana_peel": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "dispose"],
                    "state": "free"
                }
            },
            "neighbor": ["bathroom", "bedroom", "corridor_1"]
        },
        "kitchen": {
            "items": {
                "mainboard": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free"
                },
                "knife": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "place_on"],
                    "state": "free"
                },
                "fork": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "place_on"],
                    "state": "free"
                },
                "spoon": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "place_on"],
                    "state": "free"
                },
                "oven": {
                    "accessible": True,
                    "affordance": ["turnon", "turnoff","open","close"],
                    "state": "closed, power_off"
                },
                "rubbish_bin": {
                    "accessible": True,
                    "affordance": ["dispose"],
                    "state": "free"
                },
                "fridge": {
                    "accessible": True,
                    "affordance": ["open", "close"],
                    "state": "closed"
                },
                "coffee_machine": {
                    "accessible": True,
                    "affordance": ["turnon", "turnoff"],
                    "state": "power_off"
                },
                "wash_machine": {
                    "accessible": True,
                    "affordance": ["open", "close", "turnon", "turnoff"],
                    "state": "closed, power_off"
                }
            },
            "neighbor": ["corridor_1"]
        },
        "living_room": {
            "items": {
                "plate": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "place_on"],
                    "state": "free"
                },
                "couch_1": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free"
                },
                "couch_2": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free"
                },
                "robot_hub": {
                    "accessible": True,
                    "affordance": ["charge"],
                    "state": "free"
                }
            },
            "neighbor": ["dining_room"]
        },
    },
    "agent": {
        "position": "living_room",
        "state": "hand-free, battery-full"
    },
    "human": {
        "name": "Tom",
        "position": "bedroom",
        "state": "hand-free"
    },
}

ROSSER = {
    "name": "rosser",
    "rooms": {
        "bathroom": {
            "items": {
                "sink_1": {
                    "accessible": True,
                    "affordance": ["clean_mop"],
                    "state": "free"
                },
                "toilet": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free"
                },
                "detergent": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free"
                }
            },
            "neighbor": ["closet"]
        },
        "bedroom": {
            "items": {
                "bed": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free"
                },
                "tv": {
                    "accessible": True,
                    "affordance": ["turnon", "turnoff"],
                    "state": "free"
                },
                "mainboard": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free"
                },
                "ram": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free"
                },
                "spoon": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "place_on"],
                    "state": "free"
                },
                "flower": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "place_on"],
                    "state": "free"
                },
                "locker": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "open","close","load", "unload"],
                    "state": "closed, loaded",
                    "content": {
                        "paper": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free"
                        }
                    }
                },
                "shelf": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "open","close","load", "unload"],
                    "state": "closed, loaded",
                    "content": {
                        "book": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free"
                        }
                    }
                }
            },
            "neighbor": ["closet", "home_office", "living_room"]
        },
        "closet": {
            "items": {
               "clothes": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free, not-clean"
                },
                "gpu": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free"
                },
                "fork": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "place_on"],
                    "state": "free"
                },
                "glass": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "place_on"],
                    "state": "free"
                },
                "lamp": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free"
                }
            },
            "neighbor": ["bathroom", "bedroom"]
        },
        "home_office": {
            "items": {
                "chair": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free"
                },
                "cpu": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free"
                },
                "rotting_apple": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "dispose"],
                    "state": "free"
                },
                "robot_hub": {
                    "accessible": True,
                    "affordance": ["charge"],
                    "state": "free"
                },
                "knife": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "place_on"],
                    "state": "free"
                }
            },
            "neighbor": ["bedroom", "living_room"]
        },
        "kitchen": {
            "items": {
                "microwave": {
                    "accessible": True,
                    "affordance": ["open", "close", "turnon", "turnoff"],
                    "state": "closed, power_off"
                },
                "oven": {
                    "accessible": True,
                    "affordance": ["turnon", "turnoff","open","close"],
                    "state": "closed, power_off"
                },
                "sink_2": {
                    "accessible": True,
                    "affordance": ["clean_mop"],
                    "state": "free"
                },
                "fridge": {
                    "accessible": True,
                    "affordance": ["open", "close"],
                    "state": "closed, power_off"
                },
                "mug": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free"
                },
                "coffee_machine": {
                    "accessible": True,
                    "affordance": ["turnon", "turnoff"],
                    "state": "power_off"
                },
                "psu": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free"
                },
                "mop": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "clean_mop", "mop_floor"],
                    "state": "clean"
                },
                "banana_peel": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "dispose"],
                    "state": "free"
                },
                "rubbish_bin": {
                    "accessible": True,
                    "affordance": ["dispose"],
                    "state": "free"
                },
                "plate": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "place_on"],
                    "state": "free"
                }
            },
            "neighbor": ["living_room"]
        },
        "living_room": {
            "items": {
                 "desk": {
                    "accessible": True,
                    "affordance": [],
                    "state": "free"
                },
                "couch": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free"
                },
                "wash_machine": {
                    "accessible": True,
                    "affordance": ["open", "close", "turnon", "turnoff"],
                    "state": "closed, power_off"
                },
                "ssd": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free"
                },
                "cola_can": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "dispose"],
                    "state": "free"
                },
                "dining_table": {
                    "accessible": True,
                    "affordance": [],
                    "state": "free"
                }
            },
            "neighbor": ["bedroom", "home_office", "kitchen"]
        }
    },
    "agent": {
        "position": "living_room",
        "state": "hand-free, battery-full"
    },
    "human": {
        "name": "Tom",
        "position": "bedroom",
        "state": "hand-free"
    },
}

SHELBIANA = {
    "name": "shelbiana",
    "rooms": {
        "bathroom_1": {
            "items": {
                "mainboard": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free"
                },
                "sink_1": {
                    "accessible": True,
                    "affordance": ["clean_mop"],
                    "state": "free"
                },
                "toilet_1": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free"
                },
                "mop": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "clean_mop", "mop_floor"],
                    "state": "clean"
                }
            },
            "neighbor": ["lobby"]
        },
        "bathroom_2": {
            "items": {
                "psu": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free"
                },
                "sink_2": {
                    "accessible": True,
                    "affordance": ["clean_mop"],
                    "state": "free"
                },
                "toilet_2": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free"
                },
                "detergent": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free"
                }
            },
            "neighbor": ["corridor_2"]
        },
        "balcony": {
            "items": {
                "dining_table": {
                    "accessible": True,
                    "affordance": [],
                    "state": "free"
                }
            },
            "neighbor": ["living_room", "bedroom_3"]
        },
        "closet": {
            "items": {
                "gpu": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free"
                },
                "chair": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free"
                },
                "locker": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "open","close","load", "unload"],
                    "state": "closed, loaded",
                    "content": {
                        "paper": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free"
                        }
                    }
                }
            },
            "neighbor": ["corridor_2"]
        },
        "corridor_1": {
            "items": {},
            "neighbor": ["corridor_2", "kitchen", "living_room"]
        },
        "corridor_2": {
            "items": {
                "glass": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "place_on"],
                    "state": "free"
                }
            },
            "neighbor": ["bathroom_2", "bedroom_2", "bedroom_3", "closet", "corridor_1"]
        },
        "living_room": {
            "items": {
                "cola_can": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "dispose"],
                    "state": "free"
                },
                "banana_peel": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "dispose"],
                    "state": "free"
                },
                "plate": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "place_on"],
                    "state": "free"
                },
                "couch": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free"
                },
                "desk": {
                    "accessible": True,
                    "affordance": [],
                    "state": "free"
                },
                "clothes": {                                         ##clothes
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free, not-clean"
                }
            },
            "neighbor": ["balcony", "corridor_1", "lobby"]
        },
        "bedroom_1": {
            "items": {
                "cpu": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free"
                },
                "bed_1": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free"
                }
            },
            "neighbor": ["lobby"]
        },
        "bedroom_2": {
            "items": {
                "ssd": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free"
                },
                "kite_1": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free"
                },
                "rotting_apple": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "dispose"],
                    "state": "free"
                },
                "lamp": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free"
                },
            },
            "neighbor": ["corridor_2"]
        },
        "bedroom_3": {
            "items": {
                "bed_2": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free"
                },
                "kite_2": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free"
                },
                "robot_hub": {
                    "accessible": True,
                    "affordance": ["charge"],
                    "state": "free"
                }
            },
            "neighbor": ["balcony", "corridor_2"]
        },
        "lobby": {
            "items": {
                "flower": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "place_on"],
                    "state": "free"
                },
                "clock": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free"
                },
                "shelf": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "open","close","load", "unload"],
                    "state": "closed, loaded",
                    "content": {
                        "book": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free"
                        }
                    }
                }
            },
            "neighbor": ["bathroom_1", "bedroom_1", "living_room"]
        },
        "kitchen": {
            "items": {
                "ram": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free"
                },
                "knife": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "place_on"],
                    "state": "free"
                },
                "fork": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "place_on"],
                    "state": "free"
                },
                "spoon": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "place_on"],
                    "state": "free"
                },
                "microwave": {
                    "accessible": True,
                    "affordance": ["open", "close", "turnon", "turnoff"],
                    "state": "closed, power_off"
                },
                "oven": {
                    "accessible": True,
                    "affordance": ["turnon", "turnoff","open","close"],
                    "state": "closed, power_off"
                },
                "sink_3": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free"
                },
                "fridge": {
                    "accessible": True,
                    "affordance": ["open", "close"],
                    "state": "closed, power_off"
                },
                "rubbish_bin": {
                    "accessible": True,
                    "affordance": ["dispose"],
                    "state": "free"
                },
                "mug": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free"
                },
                "coffee_machine": {
                    "accessible": True,
                    "affordance": ["turnon", "turnoff"],
                    "state": "power_off"
                },
                "wash_machine": {
                    "accessible": True,
                    "affordance": ["open", "close", "turnon", "turnoff"],
                    "state": "closed, power_off"
                },
            },
            "neighbor": ["corridor_1"]
        }
    },
    "agent": {
        "position": "bedroom_3",
        "state": "battery-full, battery-full"
    },
    "human": {
        "name": "Tom",
        "position": "bedroom_1",
        "state": "hand-free"
    },
}

OFFICE = {
    "name": "office",
    "rooms": {
        "peters_office": {
            "assets": {
                "cabinet_2": {
                    "accessible": True,
                    "affordance": ["open", "close"],
                    "state": "closed",
                    "items": {
                        "phone": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "in"
                        },
                        "apple_3": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "in"
                        },
                        "stapler_1": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "in"
                        },
                        "ssd": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "in"
                        }
                    }
                },
                "desk_2": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free",
                    "items": {
                        "mainboard": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "on"
                        }
                    },
                }
            },
            "neighbor": ["corridor_1"]
        },
        "tobis_office": {
            "assets": {
                "desk_38": {
                    "accessible": True,
                    "affordance": [],
                    "state": "free",
                    "items": {
                        "pepsi": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "on"
                        },
                        "cpu": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "on"
                        }
                    },
                },
            },
            "neighbor": ["corridor_1"]
        },
        "meeting_room_1": {
            "assets": {
                "chair_3": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free",
                    "items": {},
                },
                "chair_4": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free",
                    "items": {},
                },
                "chair_5": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free",
                    "items": {},
                },
                "table_5": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free",
                    "items": {
                        "gpu": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "on"
                        },
                        "cola_can": {
                            "accessible": True,
                            "affordance": ["pick", "drop", "dispose"],
                            "state": "free",
                            "relation": "on"
                        }         
                    },
                },
                "locker": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "open","close","load", "unload"],
                    "state": "closed, loaded",
                    "items": {
                        "paper": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "in"
                        }
                    }
                }
            },
            "neighbor": ["corridor_2"]
        },
        "postdoc_bay_1": {
            "assets": {
                "desk_31": {
                    "accessible": True,
                    "affordance": [],
                    "state": "free",
                    "items": {
                        "fire_extinguisher_1": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "on"
                        },
                    },
                },
                "desk_32": {
                    "accessible": True,
                    "affordance": [],
                    "state": "free",
                    "items": {
                        "frame_1": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "on"
                        },
                        "frame_2": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "on"
                        },
                        "tshirt_7": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "on"
                        },
                        "tshirt_8": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "on"
                        },
                    },
                },
            },
            "neighbor": ["corridor_4"]
        },
        "phd_bay_1": {
            "assets": {
                "desk_7": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free",
                    "items": {},
                },
                "desk_8": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free",
                    "items": {},
                },
                "desk_9": {
                    "accessible": True,
                    "affordance": [],
                    "state": "free",
                    "items": {
                        "tshirt_1": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "on"
                        },
                    },
                },
                "desk_10": {
                    "accessible": True,
                    "affordance": [],
                    "state": "free",
                    "items": {
                        "tshirt_2": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "on"
                        },
                    },
                },
                "desk_11": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free",
                    "items": {},
                },
                "desk_12": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free",
                    "items": {},
                },
            },
            "neighbor": ["corridor_6"]
        },
        "phd_bay_2": {
            "assets": {
                "desk_13": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free",
                    "items": {},
                },
                "desk_14": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free",
                    "items": {},
                },
                "desk_15": {
                    "accessible": True,
                    "affordance": [],
                    "state": "free",
                    "items": {
                        "tshirt_3": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "on"
                        },
                    },
                },
                "desk_16": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free",
                    "items": {},
                },
                "desk_17": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free",
                    "items": {},
                },
                "desk_18": {
                    "accessible": True,
                    "affordance": [],
                    "state": "free",
                    "items": {
                        "tshirt_4": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "on"
                        },
                        "tshirt_6": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "on"
                        },
                    },
                },
            },
            "neighbor": ["corridor_17"]
        },
        "admin": {
            "assets": {},
            "neighbor": ["corridor_18"]
        },
        "printing_zone_2": {
            "assets": {
                "printer_2": {
                    "accessible": True,
                    "affordance": ["turnon", "turnoff"],
                    "state": "power_off",
                    "items": {
                        "document": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "on"
                        },
                    },
                },
            },
            "neighbor": ["corridor_3"]
        },
        "meeting_room_2": {
            "assets": {
                "chair_2": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free",
                    "items": {},
                },

            },
            "neighbor": ["corridor_5"]
        },
        "robot_lounge_2": {
            "assets": {},
            "neighbor": ["corridor_9"]
        },
        "robot_lounge_1": {
            "assets": {},
            "neighbor": ["corridor_3"]
        },
        "nikos_office": {
            "assets": {
                "chair_1": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free",
                    "items": {},
                },
                "cabinet_1": {
                    "accessible": True,
                    "affordance": ["open", "close"],
                    "state": "closed",
                    "items": {},
                },
                "desk_1": {
                    "accessible": True,
                    "affordance": [],
                    "state": "free",
                    "items": {
                        "mug": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "on"
                        },
                    },
                },
            },
            "neighbor": ["corridor_5"]
        },
        "michaels_office": {
            "assets": {
                "desk_6": {
                    "accessible": True,
                    "affordance": [],
                    "state": "free",
                    "items": {
                        "scissorss": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "on"
                        },
                        "clothes": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free, not-clean",
                            "relation": "on"
                        }
                    },
                },
                "cabinet_6": {
                    "accessible": True,
                    "affordance": ["open", "close"],
                    "state": "closed",
                    "items": {
                        "stapler_3": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "in"
                        },
                        "poster": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "in"
                        },
                    },
                },
            },
            "neighbor": ["corridor_7"]
        },
        "aarons_office": {
            "assets": {},
            "neighbor": ["corridor_9"]
        },
        "jasons_office": {
            "assets": {
                "desk_5": {
                    "accessible": True,
                    "affordance": [],
                    "state": "free",
                    "items": {
                        "monitor": {
                            "accessible": False,
                            "affordance": [],
                            "state": "free",
                            "relation": "on"
                        },
                    },
                },
                "cabine_5": {
                    "accessible": True,
                    "affordance": ["open", "close"],
                    "state": "closed",
                    "items": {},
                },
            },
            "neighbor": ["corridor_13"]
        },
        "mobile_robotics_lab": {
            "assets": {
                "table_4": {
                    "accessible": True,
                    "affordance": [],
                    "state": "free",
                    "items": {
                        "book_2": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "on"
                        },
                    },
                },
            },
            "neighbor": ["corridor_8"]
        },
        "manipulation_lab": {
            "assets": {
                "table_3": {
                    "accessible": True,
                    "affordance": [],
                    "state": "free",
                    "items": {
                        "book_1": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "on"
                        },
                        "gripper": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "on"
                        },
                        "lamp": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "on"
                        }
                    }   
                }
            },
            "neighbor": ["corridor_15"]
        },
        "phd_bay_4": {
            "assets": {
                "desk_25": {
                    "accessible": True,
                    "affordance": [],
                    "state": "free",
                    "items": {
                        "tshirt_5": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "in"
                        },
                    },
                },
                "desk_26": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free",
                    "items": {},
                },
                "desk_27": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free",
                    "items": {},
                },
                "desk_28": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free",
                    "items": {},
                },
                "desk_29": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free",
                    "items": {},
                },
                "desk_30": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free",
                    "items": {},
                },
            },
            "neighbor": ["corridor_19"]
        },
        "postdoc_bay_3": {
            "assets": {
                "desk_35": {
                    "accessible": True,
                    "affordance": [],
                    "state": "free",
                    "items": {
                        "doritos": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "on"
                        },
                    },
                },
                "desk_36": {
                    "accessible": True,
                    "affordance": [],
                    "state": "free",
                    "items": {
                        "marker": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "on"
                        },
                    },
                },
            },
            "neighbor": ["corridor_21"]
        },
        "meeting_room_4": {
            "assets": {
                "table_2": {
                    "accessible": True,
                    "affordance": [],
                    "state": "free",
                    "items": {
                        "janga": {
                            "accessible": False,
                            "affordance": [],
                            "state": "free",
                            "relation": "on"
                        },
                        "risk": {
                            "accessible": False,
                            "affordance": [],
                            "state": "free",
                            "relation": "on"
                        },
                        "monopoly": {
                            "accessible": False,
                            "affordance": [],
                            "state": "free",
                            "relation": "on"
                        },
                    },
                },
            },
            "neighbor": ["corridor_20"]
        },
        "filipes_office": {
            "assets": {
                "desk_37": {
                    "accessible": True,
                    "affordance": [],
                    "state": "free",
                    "items": {
                        "stapler_2": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "in"
                        },
                    },
                },
            },
            "neighbor": ["corridor_10"]
        },
        "luis_office": {
            "assets": {},
            "neighbor": ["corridor_10"]
        },
        "wills_office": {
            "assets": {
                "desk_4": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free",
                    "items": {
                        "ram": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "on"
                }
                    },
                },
                "cabinet_4": {
                    "accessible": True,
                    "affordance": ["open", "close"],
                    "state": "closed",
                    "items": {
                        "apple_1": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "in"
                        },
                        "thesis_1": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "in"
                        },
                        "drone_2": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "in"
                        },
                    },
                },
            },
            "neighbor": ["corridor_10"]
        },
        "phd_bay_3": {
            "assets": {
                "desk_19": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free",
                    "items": {},
                },
                "desk_20": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free",
                    "items": {},
                },
                "desk_21": {
                    "accessible": True,
                    "affordance": [],
                    "state": "free",
                    "items": {
                        "drone_1": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "in"
                        },
                    },
                },
                "desk_22": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free",
                    "items": {},
                },
                "desk_23": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free",
                    "items": {},
                },
                "desk_24": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free",
                    "items": {},
                },
            },
            "neighbor": ["corridor_11"]
        },
        "postdoc_bay_2": {
            "assets": {
                "desk_33": {
                    "accessible": True,
                    "affordance": [],
                    "state": "free",
                    "items": {
                        "frame_3": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "in"
                        },
                    },
                },
                "desk_34": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free",
                    "items": {},
                },
            },
            "neighbor": ["corridor_12"]
        },
        "lobby": {
            "assets": {
                "parcel": {
                    "accessible": True,
                    "affordance": ["pick", "drop"],
                    "state": "free",
                    "relation": "on"
                },
                "shelf": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "load", "unload"],
                    "state": "closed, loaded",
                    "items": {
                        "book_3": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free"
                        }
                    },
                },
                "flower": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "place_on"],
                    "state": "free"
                }
            },
            "neighbor": ["corridor_14"]
        },
        "supplies_station": {
            "assets": {
                "cupboard_1": {
                    "accessible": True,
                    "affordance": ["open", "close"],
                    "state": "closed",
                    "items": {
                        "printer_paper": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "in"
                        },
                        "paper_towel": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "in"
                        },
                    },
                },
                "cupboard_2": {
                    "accessible": True,
                    "affordance": ["open", "close"],
                    "state": "closed",
                    "items": {
                        "vodka": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "in"
                        },
                        "orange_juice": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "in"
                        },
                        "biscuits": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "in"
                        },
                        "bottle_water_1": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "in"
                        },
                        "bottle_water_2": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "in"
                        },
                        "bottle_water_3": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "in"
                        },
                        "bottle_water_4": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "in"
                        },
                        "bottle_water_5": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "in"
                        },
                    },
                },
            },
            "neighbor": ["corridor_24"]
        },
        "printing_zone_1": {
            "assets": {},
            "neighbor": ["corridor_24"]
        },
        "ajays_office": {
            "assets": {},
            "neighbor": ["corridor_23"]
        },
        "chris_office": {
            "assets": {},
            "neighbor": ["corridor_22"]
        },
        "lauriannes_office": {
            "assets": {},
            "neighbor": ["corridor_22"]
        },
        "dimitys_office": {
            "assets": {
                "desk_3": {
                    "accessible": True,
                    "affordance": [],
                    "state": "free",
                    "items": {
                        "K31X": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "in"
                        },
                        "buzzer": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "in"
                        }
                    },
                },
                "cabinet_3": {
                    "accessible": True,
                    "affordance": ["open", "close"],
                    "state": "closed",
                    "items": {
                        "apple_2": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "in"
                        }
                    },
                },
            },
            "neighbor": ["corridor_22"]
        },
        "meeting_room_3": {
            "assets": {
                "table_1": {
                    "accessible": True,
                    "affordance": [],
                    "state": "free",
                    "items": {
                        "headphones": {
                            "accessible": False,
                            "affordance": [],
                            "state": "free",
                            "relation": "on"
                        },
                        "rotting_apple": {
                            "accessible": True,
                            "affordance": ["pick", "drop", "dispose"],
                            "state": "free",
                            "relation": "on"
                        }
                    },
                },
                "table_6": {
                    "accessible": False,
                    "affordance": [],
                    "state": "free",
                    "items": {
                        "psu": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "on"
                }
                    },
                },
            },
            "neighbor": ["corridor_26"]
        },
        "agriculture_lab": {
            "assets": {
                "produce_container": {
                    "accessible": True,
                    "affordance": ["open", "close"],
                    "state": "closed",
                    "items": {
                        "kale_leaves_1": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "on"
                        },
                    },
                },
            },
            "neighbor": ["corridor_24"]
        },
        "kitchen": {
            "assets": {
                "cabine_1": {
                    "accessible": True,
                    "affordance": ["open", "close"],
                    "state": "closed",
                    "items": {},
                },
                "fridge": {
                    "accessible": True,
                    "affordance": ["open", "close"],
                    "state": "closed",
                    "items": {
                        "banana_2": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "on"
                        },
                        "cheese": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "on"
                        },
                        "tomato": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "on"
                        },
                        "J64M": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "on"
                        },
                        "chicken_kebab": {
                            "accessible": False,
                            "affordance": [],
                            "state": "free",
                            "relation": "on"
                        },
                        "noodles": {
                            "accessible": False,
                            "affordance": [],
                            "state": "free",
                            "relation": "on"
                        },
                        "salmon_bagel": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "on"
                        },
                        "salad": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "on"
                        },
                        "carrot": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "on"
                        },
                    },
                },
                "coffee_machine": {
                    "accessible": True,
                    "affordance": ["turnon", "turnoff"],
                    "state": "power_off",
                    "items": {},
                },
                "kitchen_bench": {
                    "accessible": True,
                    "affordance": [],
                    "state": "free",
                    "items": {
                        "kale_leaves_2": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "on"
                        },
                        "orange_1": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "on"
                        },
                        "bread": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "on"
                        },
                        "butter": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "on"
                        },
                        "chips": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "on"
                        },
                        "glass": {
                            "accessible": True,
                            "affordance": ["pick", "drop", "place_on"],
                            "state": "free",
                            "relation": "on"
                        }
                    },
                },
                "dishwasher": {
                    "accessible": True,
                    "affordance": ["open", "close"],
                    "state": "closed",
                    "items": {
                        "bowl": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "in"
                        },
                        "spoon": {
                            "accessible": True,
                            "affordance": ["pick", "drop", "place_on"],
                            "state": "free",
                            "relation": "in"
                        },
                    },
                },
                "drawer": {
                    "accessible": True,
                    "affordance": ["open", "close"],
                    "state": "closed",
                    "items": {},
                },
                "microvawe": {
                    "accessible": True,
                    "affordance": ["turnon", "turnoff"],
                    "state": "power_off",
                    "items": {},
                },
                "recycling_bin": {
                    "accessible": True,
                    "affordance": ["open", "close"],
                    "state": "closed",
                    "items": {
                        "milk_catron": {
                            "accessible": False,
                            "affordance": [],
                            "state": "free",
                            "relation": "in"
                        },
                        "orange_peel": {
                            "accessible": False,
                            "affordance": [],
                            "state": "free",
                            "relation": "in"
                        },
                        "apple_core": {
                            "accessible": False,
                            "affordance": [],
                            "state": "free",
                            "relation": "in"
                        }
                    },
                },
                "rubbish_bin": {
                    "accessible": True,
                    "affordance": ["open", "close"],
                    "state": "closed",
                    "items": {
                        "plastic_bottle": {
                            "accessible": False,
                            "affordance": [],
                            "state": "free",
                            "relation": "in"
                        },
                    },
                },
                "wash_machine": {
                    "accessible": True,
                    "affordance": ["open", "close", "turnon", "turnoff"],
                    "state": "closed, power_off"
                },
                "sink": {
                    "accessible": True,
                    "affordance": ["clean_mop"],
                    "state": "free"
                },
                "mop": {
                    "accessible": True,
                    "affordance": ["pick", "drop", "clean_mop", "mop_floor"],
                    "state": "clean"
                },
            },
            "neighbor": ["corridor_25"]
        },
        "cafeteria": {
            "assets": {
                "console table": {
                    "accessible": True,
                    "affordance": [],
                    "state": "free",
                    "items": {
                        "banana_1": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "on"
                        },
                        "plate": {
                            "accessible": True,
                            "affordance": ["pick", "drop", "place_on"],
                            "state": "free",
                            "relation": "on"
                        },
                        "fork": {
                            "accessible": True,
                            "affordance": ["pick", "drop", "place_on"],
                            "state": "free",
                            "relation": "on"
                        },
                        "knife": {
                            "accessible": True,
                            "affordance": ["pick", "drop", "place_on"],
                            "state": "free",
                            "relation": "on"
                        },
                        "detergent": {
                            "accessible": True,
                            "affordance": ["pick", "drop"],
                            "state": "free",
                            "relation": "on"
                        },
                        "banana_peel": {
                            "accessible": True,
                            "affordance": ["pick", "drop", "dispose"],
                            "state": "free",
                            "relation": "on"
                        },
                    },
                },
                "dining_table": {
                        "accessible": True,
                        "affordance": [],
                        "state": "free"
                },
                "robot_hub": {
                    "accessible": True,
                    "affordance": ["charge"],
                    "state": "free"
                }
            },

            "neighbor": ["corridor_25"]
        },
        "presentation_lounge": {
            "assets": {},
            "neighbor": ["corridor_26"]
        },
        "corridor_1": {
            "neighbor": ["peters_office", "tobis_office", "corridor_2"]
        },
        "corridor_2": {
            "neighbor": ["corridor_1", "meeting_room_1", "corridor_3", "corridor_5"]
        },
        "corridor_3": {
            "neighbor": ["corridor_2", "printing_zone_2", "robot_lounge_1", "corridor_9"]
        },
        "corridor_4": {
            "neighbor": ["postdoc_bay_1", "corridor_5"]
        },
        "corridor_5": {
            "neighbor": ["corridor_2", "corridor_4", "corridor_6", "corridor_7", "meeting_room_2", "nikos_office"]
        },
        "corridor_6": {
            "neighbor": ["phd_bay_1", "corridor_5"]
        },
        "corridor_7": {
            "neighbor": ["corridor_5", "michaels_office", "corridor_8", "corridor_16", "corridor_17"]
        },
        "corridor_8": {
            "neighbor": ["corridor_7", "mobile_robotics_lab", "corridor_13"]
        },
        "corridor_9": {
            "neighbor": ["corridor_3", "robot_lounge_2", "aarons_office", "corridor_10", "corridor_11", "corridor_13"]
        },
        "corridor_10": {
            "neighbor": ["filipes_office", "luis_office", "wills_office", "corridor_9"]
        },
        "corridor_11": {
            "neighbor": ["phd_bay_3", "corridor_9"]
        },
        "corridor_12": {
            "neighbor": ["postdoc_bay_2", "corridor_13"]
        },
        "corridor_13": {
            "neighbor": ["jasons_office", "corridor_8", "corridor_9", "corridor_12", "corridor_14"]
        },
        "corridor_14": {
            "neighbor": ["lobby", "corridor_13", "corridor_23"]
        },
        "corridor_15": {
            "neighbor": ["manipulation_lab", "corridor_18", "corridor_23"]
        },
        "corridor_16": {
            "neighbor": ["corridor_7", "corridor_17", "corridor_18"]
        },
        "corridor_17": {
            "neighbor": ["phd_bay_2", "corridor_7", "corridor_16", "corridor_18"]
        },
        "corridor_18": {
            "neighbor": ["admin", "corridor_15", "corridor_16", "corridor_19"]
        },
        "corridor_19": {
            "neighbor": ["phd_bay_4", "corridor_18", "corridor_20"]
        },
        "corridor_20": {
            "neighbor": ["meeting_room_4", "corridor_19", "corridor_21"]
        },
        "corridor_21": {
            "neighbor": ["postdoc_bay_3", "corridor_20", "corridor_22"]
        },
        "corridor_22": {
            "neighbor": ["chris_office", "lauriannes_office", "dimitys_office", "corridor_21", "corridor_23"]
        },
        "corridor_23": {
            "neighbor": ["ajays_office", "corridor_14", "corridor_15", "corridor_22", "corridor_24"]
        },
        "corridor_24": {
            "neighbor": ["supplies_station", "printing_zone_1", "agriculture_lab", "corridor_23", "corridor_25"]
        },
        "corridor_25": {
            "neighbor": ["kitchen", "cafeteria", "corridor_24", "corridor_26"]
        },
        "corridor_26": {
            "neighbor": ["meeting_room_3", "presentation_lounge", "corridor_25"]
        },
    },
    "agent": {
        "position": "mobile_robotics_lab",
        "state": "hand-free, battery-full"
    },
    "human": {
        "name": "Tom",
        "position": "meeting_room_1",
        "state": "hand-free"
    },
}

VIRTUALHOME = {
    "name": "virtualhome",
    "rooms": {
        "bathroom": {
            "assets": {
                "bathtub_39": {
                    "accessible": True,
                    "affordance": ["sit", "lie"],
                    "state": "free",
                    "items": {}
                },
                "towelrack_40": {
                    "accessible": True,
                    "affordance": ["support", "grab", "move"],
                    "state": "free",
                    "items": {}
                },
                "towelrack_41": {
                    "accessible": True,
                    "affordance": ["support", "grab", "move"],
                    "state": "free",
                    "items": {}
                },
                "towelrack_42": {
                    "accessible": True,
                    "affordance": ["support", "grab", "move"],
                    "state": "free",
                    "items": {}
                },
                "towelrack_43": {
                    "accessible": True,
                    "affordance": ["support", "grab", "move"],
                    "state": "free",
                    "items": {}
                },
                "wallshelf_44": {
                    "accessible": True,
                    "affordance": [],
                    "state": "free",
                    "items": {
                        "plate_62": {
                            "accessible": True,
                            "affordance": ["support", "grab", "recipient", "move"],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        },
                        "candle_70": {
                            "accessible": True,
                            "affordance": ["grab", "switchon", "switchoff", "move"],
                            "state": "power_off",
                            "items": {},
                            "relation": "on"
                        }
                    }
                },
                "stall_45": {
                    "accessible": True,
                    "affordance": [],
                    "state": "free",
                    "items": {}
                },
                "toilet_46": {
                    "accessible": True,
                    "affordance": ["sit", "open", "close", "contain"],
                    "state": "closed",
                    "items": {}
                    },
                "stall_47": {
                    "accessible": True,
                    "affordance": [],
                    "state": "free",
                    "items": {}
                },
                "bathroomcabinet_49": {
                    "accessible": True,
                    "affordance": ["support", "open", "close", "contain"],
                    "state": "closed",
                    "items": {}
                },
                "hairproduct_59": {
                    "accessible": True,
                    "affordance": ["grab", "pour", "open", "close", "move"],
                    "state": "closed",
                    "items": {}
                },
                "hairproduct_60": {
                    "accessible": True,
                    "affordance": ["grab", "pour", "open", "close", "move"],
                    "state": "closed",
                    "items": {}
                },
                "facecream_61": {
                    "accessible": True,
                    "affordance": ["grab", "pour", "move", "cream"],
                    "state": "free",
                    "items": {}
                },
                "towel_68": {
                    "accessible": True,
                    "affordance": ["grab", "cover_object", "move"],
                    "state": "free",
                    "items": {}
                },
                "towel_69": {
                    "accessible": True,
                    "affordance": ["grab", "cover_object", "move"],
                    "state": "free",
                    "items": {}
                },
                "lightswitch_72": {
                    "accessible": True,
                    "affordance": ["switchon", "switchoff", "has_plug"],
                    "state": "power_on",
                    "items": {}
                },
                "washingmachine_73": {
                    "accessible": True,
                    "affordance": ["recipient", "open", "close", "switchon", "switchoff", "contain", "has_plug"],
                    "state": "closed, power_off",
                    "items": {}
                }
            },
            "neighbor": ["bedroom"]
        },
        "bedroom": {
            "assets": {
                "garbagecan_105": {
                    "accessible": True,
                    "affordance": ["open", "close", "contain", "move"],
                    "state": "closed",
                    "items": {}
                },
                "bookshelf_107": {
                    "accessible": True,
                    "affordance": ["support", "contain"],
                    "state": "free",
                    "items": {
                        "book_192": {
                            "accessible": True,
                            "affordance": ["grab", "cut", "open", "close", "read", "has_paper", "move"],
                            "state": "closed",
                            "items": {},
                            "relation": "on"
                        },
                        "folder_205": {
                            "accessible": True,
                            "affordance": ["grab", "open", "close", "read", "contain", "has_paper", "move"],
                            "state": "closed",
                            "items": {},
                            "relation": "on"
                        },
                        "folder_206": {
                            "accessible": True,
                            "affordance": ["grab", "open", "close", "read", "contain", "has_paper", "move"],
                            "state": "closed",
                            "items": {},
                            "relation": "on"
                        }
                    }
                },
                "chair_109": {
                    "accessible": True,
                    "affordance": ["support", "grab", "sit", "move"],
                    "state": "free",
                    "items": {}
                },
                "desk_110": {
                    "accessible": True,
                    "affordance": ["support", "open", "close", "move"],
                    "state": "closed",
                    "items": {
                        "mousemat_173": {
                            "accessible": True,
                            "affordance": ["support", "move"],
                            "state": "free",
                            "items": {},
                            "relation": "on"    
                        },
                        "mouse_172": {
                                    "accessible": True,
                                    "affordance": ["grab", "has_plug", "move"],
                                    "state": "free",
                                    "items": {},
                                    "relation": "on"
                                },    
                        "keyboard_174": {
                            "accessible": True,
                            "affordance": ["grab", "has_plug", "move"],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        },
                        "cpuscreen_177": {
                            "accessible": True,
                            "affordance": [],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        },
                        "plate_195": {
                            "accessible": True,
                            "affordance": ["support", "grab", "recipient", "move"],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        },
                        "mug_196": {
                            "accessible": True,
                            "affordance": ["grab", "recipient", "pour", "move"],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        },
                        "cupcake_197": {
                            "accessible": True,
                            "affordance": ["grab", "eat", "move"],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        },
                        "cupcake_198": {
                            "accessible": True,
                            "affordance": ["grab", "eat", "move"],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        }
                    }
                },
                "chair_112": {
                    "accessible": True,
                    "affordance": ["support", "grab", "sit", "move"],
                    "state": "free",
                    "items": {},
                },
                "coffeetable_113": {
                    "accessible": True,
                    "affordance": ["support", "move"],
                    "state": "free",
                    "items": {
                        "candle_183": {
                            "accessible": True,
                            "affordance": ["grab", "switchon", "switchoff", "move"],
                            "state": "power_off",
                            "items": {},
                            "relation": "on"
                        },
                        "orchid_184": {
                            "accessible": True,
                            "affordance": [],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        },
                        "cellphone_190": {
                            "accessible": True,
                            "affordance": ["grab", "switchon", "switchoff", "has_plug", "move"],
                            "state": "power_off",
                            "items": {},
                            "relation": "on"
                        },
                        "wineglass_199": {
                            "accessible": True,
                            "affordance": ["grab", "recipient", "pour", "move"],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        },
                        "wineglass_200": {
                            "accessible": True,
                            "affordance": ["grab", "recipient", "pour", "move"],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        },
                        "plate_201": {
                            "accessible": True,
                            "affordance": ["support", "grab", "recipient", "move"],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        },
                        "cellphone_204": {
                            "accessible": True,
                            "affordance": ["grab", "switchon", "switchoff", "has_plug", "move"],
                            "state": "power_off",
                            "items": {},
                            "relation": "on"
                        }
                    }
                },
                "closet_114": {
                    "accessible": True,
                    "affordance": ["open", "close", "contain"],
                    "state": "closed",
                    "items": {}
                },
                "closetdrawer_127": {
                    "accessible": True,
                    "affordance": [],
                    "state": "free",
                    "items": {}
                },
                "closetdrawer_128": {
                    "accessible": True,
                    "affordance": [],
                    "state": "free",
                    "items": {}
                },
                "closet_129": {
                    "accessible": True,
                    "affordance": ["open", "close", "contain"],
                    "state": "closed",
                    "items": {}
                },
                "clothespants_141": {
                    "accessible": True,
                    "affordance": ["grab", "hang", "clothes", "move"],
                    "state": "not-clean",
                    "items": {}
                },
                "doorjamb_171": {
                    "accessible": True,
                    "affordance": [],
                    "state": "free",
                    "items": {}
                },
                "lightswitch_175": {
                    "accessible": True,
                    "affordance": ["switchon", "switchoff", "has_plug"],
                    "state": "power_on",
                    "items": {}
                },
                "computer_176": {
                    "accessible": True,
                    "affordance": ["switchon", "switchoff", "look"],
                    "state": "power_off",
                    "items": {}
                },
                "radio_178": {
                    "accessible": True,
                    "affordance": ["support", "grab", "open", "close", "switchon", "switchoff", "has_plug", "move"],
                    "state": "power_off",
                    "items": {}
                },
                "nightstand_106": {
                    "accessible": True,
                    "affordance": ["support", "open", "close", "contain"],
                    "state": "closed",
                    "items": {
                        "tablelamp_103": {
                            "accessible": True,
                            "affordance": ["switchon", "switchoff", "has_plug"],
                            "state": "power_on",
                            "items": {},
                            "relation": "on"
                        }
                    },
                },
                "nightstand_108": {
                    "accessible": True,
                    "affordance": ["support", "open", "close", "contain"],
                    "state": "closed",
                    "items": {
                        "tablelamp_104": {
                            "accessible": True,
                            "affordance": ["switchon", "switchoff", "has_plug"],
                            "state": "power_on",
                            "items": {},
                            "relation": "on"
                        }
                    },
                },
                "bed_111": {
                    "accessible": True,
                    "affordance": ["support", "sit", "lie"],
                    "state": "free",
                    "items": {
                        "pillow_188": {
                            "accessible": True,
                            "affordance": ["grab", "move"],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        },
                        "pillow_189": {
                            "accessible": True,
                            "affordance": ["grab", "move"],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        }
                },
                },
                "slippers_202": {
                    "accessible": True,
                    "affordance": ["grab", "hang", "clothes", "move"],
                    "state": "free",
                    "items": {},
                },
                "slippers_203": {
                    "accessible": True,
                    "affordance": ["grab", "hang", "clothes", "move"],
                    "state": "free",
                    "items": {},
                },
                "photoframe_191": {
                    "accessible": True,
                    "affordance": [],
                    "state": "free",
                    "items": {}
                },
                "book_193": {
                    "accessible": True,
                    "affordance": ["grab", "cut", "open", "close", "read", "has_paper", "move"],
                    "state": "closed",
                    "items": {}
                },
            },
            "neighbor": ["bathroom","kitchen"]
        },
        "kitchen": {
            "assets": {
                "tvstand_230": {
                    "accessible": True,
                    "affordance": ["support", "move"],
                    "state": "free",
                    "items": {
                        "orchid_261": {
                            "accessible": True,
                            "affordance": [],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        },
                        "tv_265": {
                            "accessible": True,
                            "affordance": ["switchon", "switchoff", "look", "has_plug"],
                            "state": "power_off",
                            "items": {},
                            "relation": "on"
                        },
                        "wineglass_299": {
                            "accessible": True,
                            "affordance": ["grab", "recipient", "pour", "move"],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        },
                        "wineglass_300": {
                            "accessible": True,
                            "affordance": ["grab", "recipient", "pour", "move"],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        },
                        "photoframe_302": {
                            "accessible": True,
                            "affordance": [],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        }
                    }
                },
                "kitchentable_231": {
                    "accessible": True,
                    "affordance": ["support", "move"],
                    "state": "free",
                    "items": {
                        "book_269": {
                            "accessible": True,
                            "affordance": ["grab", "cut", "open", "close", "read", "has_paper", "move"],
                            "state": "closed",
                            "items": {},
                            "relation": "on"
                        },
                        "salmon_328": {
                            "accessible": True,
                            "affordance": ["grab", "move"],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        },
                        "waterglass_271": {
                            "accessible": True,
                            "affordance": ["grab", "recipient", "pour", "move"],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        },
                        "waterglass_275": {
                            "accessible": True,
                            "affordance": ["grab", "recipient", "pour", "move"],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        },
                        "waterglass_282": {
                            "accessible": True,
                            "affordance": ["grab", "recipient", "pour", "move"],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        },
                        "waterglass_283": {
                            "accessible": True,
                            "affordance": ["grab", "recipient", "pour", "move"],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        },
                        "whippedcream_319": {
                            "accessible": True,
                            "affordance": ["grab", "eat", "cut", "move"],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        },
                        "cutleryknife_272": {
                            "accessible": True,
                            "affordance": ["grab", "move"],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        },
                        "cutleryfork_273": {
                            "accessible": True,
                            "affordance": ["grab", "move"],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        },
                        "plate_274": {
                            "accessible": True,
                            "affordance": ["support", "grab", "recipient", "move"],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        },
                        "cutleryknife_276": {
                            "accessible": True,
                            "affordance": ["grab", "move"],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        },
                        "cutleryfork_277": {
                            "accessible": True,
                            "affordance": ["grab", "move"],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        },
                        "plate_278": {
                            "accessible": True,
                            "affordance": ["support", "grab", "recipient", "move"],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        },
                        "plate_279": {
                            "accessible": True,
                            "affordance": ["support", "grab", "recipient", "move"],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        },
                        "cutleryfork_280": {
                            "accessible": True,
                            "affordance": ["grab", "move"],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        },
                        "cutleryknife_281": {
                            "accessible": True,
                            "affordance": ["grab", "move"],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        },
                        "cutleryknife_284": {
                            "accessible": True,
                            "affordance": ["grab", "move"],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        },
                        "cutleryfork_285": {
                            "accessible": True,
                            "affordance": ["grab", "move"],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        },
                        "plate_286": {
                            "accessible": True,
                            "affordance": ["support", "grab", "recipient", "move"],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        },
                        "pie_320": {
                            "accessible": True,
                            "affordance": ["grab", "eat", "cut", "move"],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        }
                    }
                },
                "kitchencounterdrawer_245": {
                    "accessible": True,
                    "affordance": [],
                    "state": "free",
                    "items": {
                        "microwave_314": {
                            "accessible": True,
                            "affordance": ["open", "close", "switchon", "switchoff", "contain", "has_plug"],
                            "state": "closed, power_off",
                            "items": {},
                            "relation": "on"
                        },
                        "bellpepper_321": {
                            "accessible": True,
                            "affordance": ["grab", "move"],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        },
                        "bellpepper_322": {
                            "accessible": True,
                            "affordance": ["grab", "move"],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        },
                        "bellpepper_323": {
                            "accessible": True,
                            "affordance": ["grab", "move"],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        },
                        "bellpepper_324": {
                            "accessible": True,
                            "affordance": ["grab", "move"],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        },
                        "bellpepper_325": {
                            "accessible": True,
                            "affordance": ["grab", "move"],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        },
                        "faucet_249": {
                            "accessible": True,
                            "affordance": ["switchon", "switchoff"],
                            "state": "power_off",
                            "items": {},
                            "relation": "on"
                        },
                        "washingsponge_267": {
                            "accessible": True,
                            "affordance": ["grab", "move"],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        },
                        "dishwashingliquid_268": {
                            "accessible": True,
                            "affordance": ["grab", "pour", "move", "cream"],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        },
                        "coffeemaker_307": {
                            "accessible": True,
                            "affordance": ["recipient", "open", "close", "switchon", "switchoff", "contain", "has_plug", "move"],
                            "state": "power_off",
                            "items": {},
                            "relation": "on"
                        },
                        "coffeepot_308": {
                            "accessible": True,
                            "affordance": ["grab", "recipient", "open", "close", "move"],
                            "state": "closed",
                            "items": {},
                            "relation": "on"
                        },
                        "toaster_309": {
                            "accessible": True,
                            "affordance": ["switchon", "switchoff", "contain", "has_plug", "move"],
                            "state": "power_off",
                            "items": {},
                            "relation": "on"
                        },
                        "dishbowl_327": {
                            "accessible": True,
                            "affordance": ["grab", "recipient", "move"],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        }
                    }
                },
                "sink_247": {
                    "accessible": True,
                    "affordance": ["recipient", "contain"],
                    "state": "free",
                    "items": {}
                },
                "sink_248": {
                    "accessible": True,
                    "affordance": ["recipient", "contain"],
                    "state": "free",
                    "items": {}
                },
                "bookshelf_250": {
                    "accessible": True,
                    "affordance": ["support", "contain"],
                    "state": "free",
                    "items": {
                        "box_288": {
                            "accessible": True,
                            "affordance": ["grab", "recipient", "open", "close", "contain", "cover_object", "move"],
                            "state": "closed",
                            "items": {},
                            "relation": "on"
                        },
                        "dishbowl_289": {
                            "accessible": True,
                            "affordance": ["grab", "recipient", "move"],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        }
                    }
                },
                "wallshelf_251": {
                    "accessible": True,
                    "affordance": [],
                    "state": "free",
                    "items": {
                        "chips_329": {
                            "accessible": True,
                            "affordance": ["grab", "move"],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        },
                        "chips_330": {
                            "accessible": True,
                            "affordance": ["grab", "move"],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        },
                        "candybar_331": {
                            "accessible": True,
                            "affordance": ["grab", "eat", "move"],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        },
                        "chocolatesyrup_332": {
                            "accessible": True,
                            "affordance": ["grab", "eat", "cut", "move"],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        }
                    }
                },
                "wallshelf_252": {
                    "accessible": True,
                    "affordance": [],
                    "state": "free",
                    "items": {
                        "crackers_333": {
                            "accessible": True,
                            "affordance": ["grab", "move"],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        },
                        "creamybuns_334": {
                            "accessible": True,
                            "affordance": ["grab", "eat", "cut", "move"],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        },
                        "cereal_335": {
                            "accessible": True,
                            "affordance": ["grab", "eat", "move"],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        }
                    }
                },
                "lightswitch_262": {
                    "accessible": True,
                    "affordance": ["switchon", "switchoff", "has_plug"],
                    "state": "power_on",
                    "items": {}
                },
                "stovefan_305": {
                    "accessible": True,
                    "affordance": [],
                    "state": "free",
                    "items": {}
                },
                "fridge_306": {
                    "accessible": True,
                    "affordance": ["open", "close", "switchon", "switchoff", "contain", "has_plug"],
                    "state": "closed",
                    "items": {}
                },
                "breadslice_310": {
                    "accessible": True,
                    "affordance": ["grab", "eat", "cut", "move"],
                    "state": "free",
                    "items": {}
                },
                "breadslice_311": {
                    "accessible": True,
                    "affordance": ["grab", "eat", "cut", "move"],
                    "state": "free",
                    "items": {}
                },
                "stove_312": {
                    "accessible": True,
                    "affordance": ["support", "open", "close", "switchon", "switchoff", "contain"],
                    "state": "power_off, closed",
                    "items": {
                        "fryingpan_270": {
                            "accessible": True,
                            "affordance": ["support", "grab", "recipient", "contain", "move"],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        }
                    }
                },
                "oventray_313": {
                    "accessible": True,
                    "affordance": ["support", "grab", "move"],
                    "state": "free",
                    "items": {}
                },
                "bananas_316": {
                    "accessible": True,
                    "affordance": ["grab", "move"],
                    "state": "free",
                    "items": {}
                },
                "bananas_317": {
                    "accessible": True,
                    "affordance": ["grab", "move"],
                    "state": "free",
                    "items": {}
                },
                "dishbowl_318": {
                    "accessible": True,
                    "affordance": ["grab", "recipient", "move"],
                    "state": "free",
                    "items": {}
                }
            },
            "neighbor": ["bedroom","livingroom"]
        },
        "livingroom": {
            "assets": {
                "tvstand_370": {
                    "accessible": True,
                    "affordance": ["support", "move"],
                    "state": "free",
                    "items": {
                        "tv_427": {
                            "accessible": True,
                            "affordance": ["switchon", "switchoff", "look", "has_plug"],
                            "state": "power_off",
                            "items": {},
                            "relation": "on"
                        },
                        "cellphone_449": {
                            "accessible": True,
                            "affordance": ["grab", "switchon", "switchoff", "has_plug", "move"],
                            "state": "power_off",
                            "items": {},
                            "relation": "on"
                        },
                        "remotecontrol_453": {
                            "accessible": True,
                            "affordance": ["grab", "switchon", "switchoff", "move"],
                            "state": "power_off",
                            "items": {},
                            "relation": "on"
                        }
                    }
                },
                "bookshelf_371": {
                    "accessible": True,
                    "affordance": ["support", "contain"],
                    "state": "free",
                    "items": {
                        "box_436": {
                            "accessible": True,
                            "affordance": ["grab", "recipient", "open", "close", "contain", "cover_object", "move"],
                            "state": "closed",
                            "items": {},
                            "relation": "on"
                        }
                    }
                },
                "chair_373": {
                    "accessible": True,
                    "affordance": ["support", "grab", "sit", "move"],
                    "state": "free",
                    "items": {}
                },  
                "desk_374": {
                    "accessible": True,
                    "affordance": ["support", "open", "close", "move"],
                    "state": "closed",
                    "items": {
                        "mousemat_431": {
                            "accessible": True,
                            "affordance": ["support", "move"],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        },
                        "mouse_430": {
                            "accessible": True,
                            "affordance": ["grab", "has_plug", "move"],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        },
                        "keyboard_432": {
                            "accessible": True,
                            "affordance": ["grab", "has_plug", "move"],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        },
                        "computer_434": {
                            "accessible": True,
                            "affordance": ["switchon", "switchoff", "look"],
                            "state": "power_off",
                            "items": {},
                            "relation": "on"
                        },
                        "mug_448": {
                            "accessible": True,
                            "affordance": ["grab", "recipient", "pour", "move"],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        },
                        "paper_452": {
                            "accessible": True,
                            "affordance": ["grab", "read", "has_paper", "move"],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        }
                    }
                },
                "closet_375": {
                    "accessible": True,
                    "affordance": ["open", "close", "contain"],
                    "state": "closed",
                    "items": {}
                },
                "cabinet_416": {
                    "accessible": True,
                    "affordance": ["support", "open", "close", "contain"],
                    "state": "closed",
                    "items": {
                        "folder_454": {
                            "accessible": True,
                            "affordance": ["grab", "open", "close", "read", "contain", "has_paper", "move"],
                            "state": "closed",
                            "items": {},
                            "relation": "on"
                        }
                    }
                },
                "sofa_369": {
                    "accessible": True,
                    "affordance": ["support", "sit", "lie", "move"],
                    "state": "free",
                    "items": {
                        "pillow_422": {
                            "accessible": True,
                            "affordance": ["grab", "move"],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        },
                        "pillow_423": {
                            "accessible": True,
                            "affordance": ["grab", "move"],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        },
                    },
                },
                "coffeetable_372": {
                    "accessible": True,
                    "affordance": ["support", "move"],
                    "state": "free",
                    "items": {
                        "apple_438": {
                            "accessible": True,
                            "affordance": ["grab", "move"],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        },
                        "apple_439": {
                            "accessible": True,
                            "affordance": ["grab", "move"],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        },
                        "bananas_440": {
                            "accessible": True,
                            "affordance": ["grab", "move"],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        },
                        "lime_441": {
                            "accessible": True,
                            "affordance": ["grab", "move"],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        },
                        "peach_442": {
                            "accessible": True,
                            "affordance": [],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        },
                        "peach_443": {
                            "accessible": True,
                            "affordance": [],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        },
                        "plum_444": {
                            "accessible": True,
                            "affordance": ["grab", "move"],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        },
                        "plum_445": {
                            "accessible": True,
                            "affordance": ["grab", "move"],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        },
                        "dishbowl_446": {
                            "accessible": True,
                            "affordance": ["grab", "recipient", "move"],
                            "state": "free",
                            "items": {},
                            "relation": "on"
                        },
                        "cellphone_450": {
                            "accessible": True,
                            "affordance": ["grab", "switchon", "switchoff", "has_plug", "move"],
                            "state": "power_off",
                            "items": {},
                            "relation": "on"
                        }
                    }
                },
                "lightswitch_428": {
                    "accessible": True,
                    "affordance": ["switchon", "switchoff", "has_plug"],
                    "state": "power_on",
                    "items": {}
                },
            },
            "neighbor": ["kitchen"]
        }
},
    "agent": {
        "position": "kitchen",
        "state": "hand-free"
    }
}

LAB= {
    "name": "lab",
    "rooms": {
        "lab": {
            "assets": {
                "table_1": {
                    "accessible": True,
                    "affordance": [],
                    "state": "free",
                        "items": {
                            "book": {
                                "accessible": True,
                                "affordance": ["pick", "drop"],
                                "state": "free",
                                "relation": "on"
                            },
                            "bottle": {
                                "accessible": True,
                                "affordance": ["pick", "drop"],
                                "state": "free",
                                "relation": "on"
                            },
                            "box": {
                                "accessible": True,
                                "affordance": ["pick", "drop"],
                                "state": "free",
                                "relation": "on"
                            }
                        }
                },
                "table_2": {
                    "accessible": True,
                    "affordance": [],
                    "state": "free",
                        "items": {
                            "robot_arm_1": {
                                "accessible": True,
                                "affordance": [],
                                "state": "free",
                                "relation": "on"
                            }
                        }
                },
                "table_3": {
                    "accessible": True,
                    "affordance": [],
                    "state": "free",
                        "items": {
                            "robot_arm_2": {
                                "accessible": True,
                                "affordance": [],
                                "state": "free",
                                "relation": "on"
                            }
                        }
                },     
                "table_4": {
                    "accessible": True,
                    "affordance": [],
                    "state": "free",
                        "items": {
                            "keyboard": {
                                "accessible": True,
                                "affordance": ["pick", "drop"],
                                "state": "free",
                                "relation": "on"
                            },
                            "mouse": {
                                "accessible": True,
                                "affordance": ["pick", "drop"],
                                "state": "free",
                                "relation": "on"
                            }
                        }
                },
                "chair_1": {
                    "accessible": True,
                    "affordance": [],
                    "state": "free",
                    "items": {} 
                 }, 
                "chair_2": {
                    "accessible": True,
                    "affordance": [],
                    "state": "free",
                    "items": {} 
                },   
                "tv": {
                    "accessible": True,
                    "affordance": [],
                    "state": "free",
                    "items": {} 
                }
            }
        }
    },
    "agent": {
        "position": "lab",
        "state": "hand-free, battery-full"
    }
}    
    

   









