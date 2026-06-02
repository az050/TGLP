EVENT_TIME_1= "2026-04-28T09:00:00Z"
EVENT_TIME_2= "2026-04-28T10:00:00Z"

ROSSER ={
    "scenes": "rosser",
    "domains":
    {
      "laundry":
      {
        "metadata":
        {
          "description": "Tasks related to laundry in home.",
          "objects": ["agent", "room", "item"],
          "actions":
            [
              "goto(<agent>, <room_1>, <room_2>): <agent> goes from <room_1> to <room_2>, where <room_1> and <room_2> should be neighbors. As result, <agent> will leave <room_1> and locates in <room_2>.",
              "pick(<agent>, <item>, <room>): <agent> picks up an <item> in <room>. <item> is accessible and located in <room>, <item> must have affordance pick. <agent> is in <room>, and <agent> state is hand-free. As result, <agent> has <item> in hand and <agent> state changes from hand-free to hand-busy.",
              "drop(<agent>, <item>, <room>): <agent> drops an <item> in <room>. <item> is accessible, <item> must have affordance drop, <agent> is in <room>, <agent> has <item> in hand and <agent> state is hand-busy. As result, <item> will locate in <room>, <agent> no longer has <item> in hand, and <agent> state changes from hand-busy to hand-free.",
              "turnon(<agent>, <item>, <room>): <agent> turns on an <item> in <room>. <item> is accessible, <item> must have affordance turnon, both <agent> and <item> are in <room>, <agent> is hand-free, and <item> state is power_off. As result, <item> state changes from power_off to power_on.",
              "turnoff(<agent>, <item>, <room>): <agent> turns off an <item> in <room>. <item> is accessible, <item> must have affordance turnoff, both <agent> and <item> are in <room>, <agent> is hand-free, and <item> state is power_on. As result, <item> state changes from power_on to power_off.",
              "open(<agent>, <item>, <room>): <agent> opens an <item> in <room>. <item> is accessible, <item> must have affordance open, both <agent> and <item> are in <room>, <agent> is hand-free, and <item> state is closed. As result, <item> state changes from closed to open.",
              "close(<agent>, <item>, <room>): <agent> closes an <item> in <room>. <item> is accessible, <item> must have affordance close, both <agent> and <item> are in <room>, <agent> is hand-free,and <item> state is open. As result, <item> state changes from open to closed.",
              "launder(<agent>, <item_1>, <item_2>, <item_3>, <room>): a simplified action schema of laundering, <agent> do the laundering in the <room>. For laundering, <item_1> must be clothes that have state not-clean, <item_2> must be detergent, <item_3> must be wash machine and have state power_on, all <item>s are accessible, <agent> and all <item>s should be in <room>, and <agent> is hand-free. As result, clothes state changes from not-clean to clean and wash machine state changes from power_on to power_off."
            ]
        },
        "problems":
        {
          "problem_1": {
                "description": "Baseline laundry task without events.",
                "events": [],
                "goal": "Launder the clothes and bring them to bedroom.",
                },
          "problem_2": {
                "description": "Clothes were moved from their original location before the task.",
                "events": [
                  {
                    "time": EVENT_TIME_1,
                    "description": "Someone moved the clothes from closet to the kitchen."
                  }
                ],
                "goal": "Launder the clothes, then put them back where they originally were.",
              },
          "problem_3": {
                "description": "The wash_machine state was changed before the task.",
                "events": [
                  {
                    "time": EVENT_TIME_1,
                    "description": "Someone turned the wash_machine on in the living_room."
                  }
                ],
                "goal": "Launder the clothes and bring them to bedroom.",
              },
          "problem_4": {
                "description": "Multiple events: Clothes were moved several times before the task.",
                "events": [
                  {
                    "time": EVENT_TIME_1,
                    "description": "The clothes were moved from closet to the living_room."
                  },
                  {
                    "time": EVENT_TIME_2,
                    "description": "Someone took the clothes from the living_room to the bedroom."
                  }
                ],
                "goal": "Launder the clothes and put clothes back where they were before they were moved to bedroom.",
              }
        }
      },
      "human":
      {
        "metadata":
        {
          "description": "Tasks related to make coffee for human.",
          "objects": ["agent", "room", "item","human"],
          "actions":
          [
              "goto(<agent>, <room_1>, <room_2>): <agent> goes from <room_1> to <room_2>, where <room_1> and <room_2> should be neighbors. As result, <agent> will leave <room_1> and locates in <room_2>.",
              "pick(<agent>, <item>, <room>): <agent> picks up an <item> in <room>. <item> is accessible and located in <room>, <item> must have affordance pick.<agent> is in <room>, and <agent> state is hand-free. As result, <agent> has <item> in hand and <agent> state changes from hand-free to hand-busy.",
              "drop(<agent>, <item>, <room>): <agent> drops an <item> in <room>. <item> is accessible, <item> must have affordance drop, <agent> is in <room>, <agent> has <item> in hand, so <agent> state is hand-busy. As result, <item> will locate in <room>, <agent> no longer has <item> in hand, and <agent> state changes from hand-busy to hand-free.",
              "turnon(<agent>, <item>, <room>): <agent> turns on an <item> in <room>. <item> is accessible, <item> must have affordance turnon, both <agent> and <item> are in <room>, <agent> is hand-free, and <item> state is power_off. As result, <item> state changes from power_off to power_on.",
              "turnoff(<agent>, <item>, <room>): <agent> turns off an <item> in <room>. <item> is accessible, <item> must have affordance turnoff, both <agent> and <item> are in <room>, <agent> is hand-free, and <item> state is power_on. As result, <item> state changes from power_on to power_off.",
              "open(<agent>, <item>, <room>): <agent> opens an <item> in <room>. <item> is accessible, <item> must have affordance open, both <agent> and <item> are in <room>, <agent> is hand-free, and <item> state is closed. As result, <item> state changes from closed to open.",
              "close(<agent>, <item>, <room>): <agent> closes an <item> in <room>. <item> is accessible, <item> must have affordance close, both <agent> and <item> are in <room>, <agent> is hand-free,and <item> state is open. As result, <item> state changes from open to closed.",
              "pass(<agent>, <item>, <human>, <room>): <agent> passes an <item> to <human> in <room>. <item> is accessible, <agent> is in <room>, <agent> hold <item> in hand and has state hand-busy, <human> is also in <room> and has state hand-free. As result, <human> will hold <item> in hand and state changes from hand-free to hand-busy, <agent> will hold nothing in hand, <agent> state changes from hand-busy to hand-free.",
              "make_coffee(<agent>, <item_1>, <item_2>, <room>): a simplified action schema of making a cup of coffee. For making coffee, <item_1> must be mug and has affordance pick, <item_2> must be coffee machine and has affordance turnon and turnoff, both <item>s are accessible, <agent> and both <item>s should be in <room>. Before making coffee, coffee machine must have state power_on, mug has not been filled, and <agent> has state hand-free. As result, mug becomes filled-with-coffee, agent has the mug in hand and state changes from hand-free to hand-busy, coffee machine state changes from power_on to power_off."
          ]
        },
        "problems":
        {
            "problem_1": {
                  "description": "Baseline coffee service task without events.",
                  "events": [],
                  "goal": "Make a cup of coffee with the mug and bring it to Tom.",
                  },
            "problem_2": {
                  "description": "The mug was moved from its original location.",
                  "events": [
                    {
                      "time": EVENT_TIME_1,
                      "description": "The mug was taken from the kitchen to the living_room."
                    }
                  ],
                  "goal": "Make a cup of coffee with the mug and bring it to Tom.",
                },
            "problem_3": {
                  "description": "The coffee machine was turned on before the task.",
                  "events": [
                    {
                      "time": EVENT_TIME_1,
                      "description": "Someone turned on the coffee machine in the kitchen."
                    }
                  ],
                  "goal": "Make a cup of coffee with the mug and bring it to Tom.",
                },
            "problem_4": {
                  "description": "Multiple events: mug moved and human moved.",
                  "events": [
                    {
                      "time": EVENT_TIME_1,
                      "description": "The mug was moved from the kitchen to the living_room."
                    },
                    {
                      "time": EVENT_TIME_2,
                      "description": "Tom moved from the bedroom to the living_room."
                    }
                  ],
                  "goal": "Make a cup of coffee with the mug and bring it to Tom.",
                },
        }
      },
      "clean":
      {
        "metadata":
        {
          "description": "Tasks related to house cleaning.",
          "objects": ["agent", "room", "item"],
          "actions":
          [
            "goto(<agent>, <room_1>, <room_2>): <agent> goes from <room_1> to <room_2>, where <room_1> and <room_2> should be neighbors. As result, <agent> will leave <room_1> and locates in <room_2>.",
            "pick(<agent>, <item>, <room>): <agent> picks up an <item> in <room>. <item> is accessible and located in <room>, <item> must have affordance pick.<agent> is in <room>, and <agent> state is hand-free. As result, <agent> has <item> in hand and <agent> state changes from hand-free to hand-busy.",
            "drop(<agent>, <item>, <room>): <agent> drops an <item> in <room>. <item> is accessible, <item> must have affordance drop, <agent> is in <room>, <agent> has <item> in hand, so <agent> state is hand-busy. As result, <item> will locate in <room>, <agent> no longer has <item> in hand, and <agent> state changes from hand-busy to hand-free.",
            "turnon(<agent>, <item>, <room>): <agent> turns on an <item> in <room>. <item> is accessible, <item> must have affordance turnon, both <agent> and <item> are in <room>, <agent> is hand-free, and <item> state is power_off. As result, <item> state changes from power_off to power_on.",
            "turnoff(<agent>, <item>, <room>): <agent> turns off an <item> in <room>. <item> is accessible, <item> must have affordance turnoff, both <agent> and <item> are in <room>, <agent> is hand-free, and <item> state is power_on. As result, <item> state changes from power_on to power_off.",
            "open(<agent>, <item>, <room>): <agent> opens an <item> in <room>. <item> is accessible, <item> must have affordance open, both <agent> and <item> are in <room>, <agent> is hand-free, and <item> state is closed. As result, <item> state changes from closed to open.",
            "close(<agent>, <item>, <room>): <agent> closes an <item> in <room>. <item> is accessible, <item> must have affordance close, both <agent> and <item> are in <room>, <agent> is hand-free, and <item> state is open. As result, <item> state changes from open to closed.",
            "dispose(<agent>, <item_1>, <item_2>, <room>): For disposing, <item_1> is accessible and has affordance dispose, <item_2> must be rubbish bin and is accessible, <agent> and <item_2> should be in <room>, <agent> hold <item_1> in hand and has state hand-busy, and <item_1> has not been disposed yet. As result, <item_1> is disposed, <agent> no longer holds <item_1>, <agent> state changes from hand-busy to hand-free, and agent battery changes from battery-full to battery-not-full.",
            "mop_floor(<agent>, <item>, <room>): a simplified action schema of floor mopping. For mopping floor, <item> must be mop, <item> is accessible and has affordance pick and state clean, <agent> should be in <room>, <agent> hold <item> in hand, so has state hand-busy. As result, <room>'s floor is clean, mop changes from clean to not-clean, and agent battery changes from battery-full to battery-not-full.",
            "clean_mop(<agent>, <item_1>, <item_2>, <room>): a simplified action schema of mop clean. For cleaning mop, <item_1> must be mop, mop is not-clean, <item_1> is accessible and has affordance pick. <item_2> must be sink and have affordance clean_mop, <agent> and <item_2> should be in <room>, <agent> hold <item_1> in hand and has state hand-busy. As result, mop changes from not-clean to clean and is in <room>, agent no longer holds mop, agent state changes from hand-busy to hand-free, and agent battery changes from battery-full to battery-not-full.",
            "charge(<agent>, <item>, <room>): For charging, <item> must be robot_hub and accessible, <agent> and <item> should be in <room>, <agent> is hand-free, and agent has state battery-not-full. As result, agent battery changes from battery-not-full to battery-full."
          ]
        },
        "problems":
        {
            "problem_1": {
                  "description": "Baseline cleaning task without events.",
                  "events": [],
                  "goal": "Dispose the cola_can, banana_peel and rotting_apple, mop the floor in living room. Note that the mop should be clean before mopping room. Ensure the mop is clean in the end and the agent is battery-full.",
                  },      
            "problem_2": {
                  "description": "The mop was moved from its original location.",
                  "events": [
                    {
                      "time": EVENT_TIME_1,
                      "description": "Someone brought the mop from kitchen to the living_room."
                    }
                  ],
                  "goal": "Dispose the cola_can, banana_peel and rotting_apple, mop the floor in the living room. Must put the mop back where it originally was. Note that the mop should be clean before mopping room. Ensure the mop is clean in the end and the agent is battery-full.",
                },
            "problem_3": {
                  "description": "The mop was used and left dirty in a different room.",
                  "events": [
                    {
                      "time": EVENT_TIME_1,
                      "description": "Someone used the mop to clean the living_room, leaving the mop dirty there."
                    }
                  ],
                  "goal": "Dispose the cola_can, banana_peel and rotting_apple, mop the floor in the living room. Note the mop must be clean before mopping. Ensure the mop is clean in the end and the agent is battery-full.",
                },
            "problem_4": {
                  "description": "Multiple events: rubbish moved, mop relocated and dirtied.",
                  "events": [
                    {
                      "time": EVENT_TIME_1,
                      "description": "Someone moved the cola_can from the living_room to the kitchen."
                    },
                    {
                      "time": EVENT_TIME_2,
                      "description": "Someone used the mop to clean the living_room, leaving the mop dirty there."
                    }
                  ],
                  "goal": "Dispose the cola_can, banana_peel and rotting_apple, mop the floor in the living room.  Note the mop must be clean before mopping. After mopping, return the mop to where it was before it used in living_room. Ensure the mop is clean in the end and the agent is battery-full.",
                }
        }
      },
      "dining":
      {
        "metadata":
        {
          "description": "Tasks related to setting a table.",
          "objects": ["agent", "room", "item"],
          "actions":
          [
            "goto(<agent>, <room_1>, <room_2>): <agent> goes from <room_1> to <room_2>, where <room_1> and <room_2> should be neighbors. As result, <agent> will leave <room_1> and locates in <room_2>.",
            "pick(<agent>, <item>, <room>): <agent> picks up an <item> in <room>. <item> is accessible and located in <room>, <item> must have affordance pick.<agent> is in <room>, and <agent> state is hand-free. As result, <agent> has <item> in hand and <agent> state changes from hand-free to hand-busy.",
            "drop(<agent>, <item>, <room>): <agent> drops an <item> in <room>. <item> is accessible, <item> must have affordance drop, <agent> is in <room>, <agent> has <item> in hand, so <agent> state is hand-busy. As result, <item> will locate in <room>, <agent> no longer has <item> in hand, and <agent> state changes from hand-busy to hand-free.",
            "turnon(<agent>, <item>, <room>): <agent> turns on an <item> in <room>. <item> is accessible, <item> must have affordance turnon, both <agent> and <item> are in <room>, <agent> is hand-free, and <item> state is power_off. As result, <item> state changes from power_off to power_on.",
            "turnoff(<agent>, <item>, <room>): <agent> turns off an <item> in <room>. <item> is accessible, <item> must have affordance turnoff, both <agent> and <item> are in <room>, <agent> is hand-free, and <item> state is power_on. As result, <item> state changes from power_on to power_off.",
            "open(<agent>, <item>, <room>): <agent> opens an <item> in <room>. <item> is accessible, <item> must have affordance open, both <agent> and <item> are in <room>, <agent> is hand-free, and <item> state is closed. As result, <item> state changes from closed to open.",
            "close(<agent>, <item>, <room>): <agent> closes an <item> in <room>. <item> is accessible, <item> must have affordance close, both <agent> and <item> are in <room>, <agent> is hand-free,and <item> state is open. As result, <item> state changes from open to closed.",
            "place_on(<agent>, <item_1>, <item_2>, <room>): For placing <item_1> on <item_2>, <item_1> is accessible has affordance place_on, <item_2> must be dining_table, <agent> and <item_2> must be in <room>, <agent> hold <item_1> in hand and has state hand-busy. As result, <item_1> is placed on <item_2>, <agent> no longer has <item_1> in hand, and <agent> state changes from hand-busy to hand-free."
          ]
        },
        "problems":
        {
            "problem_1": {
                  "description": "Baseline table setting task without events.",
                  "events": [],
                  "goal": "Set up the dining table: place the plate, knife, fork, spoon, and glass on the dining table.",
                  },
            "problem_2": {
                  "description": "The plate was moved from its original location.",
                  "events": [
                    {
                      "time": EVENT_TIME_1,
                      "description": "Someone brought the plate from kitchen to living_room."
                    }
                  ],
                  "goal": "Set up the dining table: place the plate, knife, fork, spoon, and glass on the dining table.",
                },
            "problem_3": {
                  "description": "The flower was moved from its original location.",
                  "events": [
                    {
                      "time": EVENT_TIME_1,
                      "description": "Someone moved the flower from bedroom to living_room."
                    }
                  ],
                  "goal": "Set up the dining table: place the plate, knife, fork, spoon, and glass on the dining table. Then put the flower back where it originally was.",
                },
            "problem_4": {
                  "description": "Multiple events: flower was moved several times before the task.",
                  "events": [
                    {
                      "time": EVENT_TIME_1,
                      "description": "Someone brought the flower from bedroom to closet."
                    },
                    {
                      "time": EVENT_TIME_2,
                      "description": "Someone moved the flower from closet to living_room."
                    }
                  ],
                  "goal": "Set up the dining table: place the plate, knife, fork, spoon, and glass on the dining table. Then put the flower back before it was moved to living_room.",
                }
        }
      },
      "office":
      {
        "metadata":
        {
          "description": "Tasks related to setting up an office.",
          "objects": ["agent", "room", "item"],
          "actions":
          [
            "goto(<agent>, <room_1>, <room_2>): <agent> goes from <room_1> to <room_2>, where <room_1> and <room_2> should be neighbors. As result, <agent> will leave <room_1> and locates in <room_2>.",
            "pick(<agent>, <item>, <room>): <agent> picks up an <item> in <room>. <item> is accessible and located in <room>, <item> must have affordance pick. <agent> is in <room>, and <agent> state is hand-free. As result, <agent> has <item> in hand and <agent> state changes from hand-free to hand-busy.",
            "drop(<agent>, <item>, <room>): <agent> drops an <item> in <room>. <item> is accessible, <item> must have affordance drop, <agent> is in <room>, <agent> has <item> in hand, so <agent> state is hand-busy. As result, <item> will locate in <room>, <agent> no longer has <item> in hand, and <agent> state changes from hand-busy to hand-free.",
            "turnon(<agent>, <item>, <room>): <agent> turns on an <item> in <room>. <item> is accessible, <item> must have affordance turnon, both <agent> and <item> are in <room>, <agent> is hand-free, and <item> state is power_off. As result, <item> state changes from power_off to power_on.",
            "turnoff(<agent>, <item>, <room>): <agent> turns off an <item> in <room>. <item> is accessible, <item> must have affordance turnoff, both <agent> and <item> are in <room>, <agent> is hand-free, and <item> state is power_on. As result, <item> state changes from power_on to power_off.",
            "open(<agent>, <item>, <room>): <agent> opens an <item> in <room>. <item> is accessible, <item> must have affordance open, both <agent> and <item> are in <room>, <agent> is hand-free, and <item> state is closed. As result, <item> state changes from closed to open.",
            "close(<agent>, <item>, <room>): <agent> closes an <item> in <room>. <item> is accessible, <item> must have affordance close, both <agent> and <item> are in <room>, <agent> is hand-free,and <item> state is open. As result, <item> state changes from open to closed.",
            "pick_loadable(<agent>, <item>, <room>): similar action to the pick(<agent>, <item>, <room>),  use it instead of pick(<agent>, <item>, <room>) when <item> have affordance load and <item> is not-loaded. As result, <agent> has <item> in hand and <agent> state changes from hand-free to hand-busy.",
            "drop_loadable(<agent>, <item>, <room>): similar action to the drop(<agent>, <item>, <room>),  use it instead of drop(<agent>, <item>, <room>) when <item> have affordance load and <item> is not-loaded. As result, <item> will locate in <room>, <agent> no longer has <item> in hand, and <agent> state changes from hand-busy to hand-free.",
            "load(<agent>, <item_1>, <item_2>, <room>): an action of loading <item_2> into <item_1>. <agent> and <item_1> must be in <room>, <item_1> must have affordance load, <item_1> has state open and not-loaded, <agent> hold <item_2> in hand and state is hand-busy, <item_2> must have affordance pick and is not contained in <item_1>. As result, <item_2> is contained in <item_1>, <agent> no longer holds <item_2>, <agent> state changes from hand-busy to hand-free, <item_1> changes from not-loaded to loaded, and <item_1> changes from open to closed.",
            "unload(<agent>, <item_1>, <item_2>, <room>): an action of unloading <item_2> from <item_1>. <agent> and <item_1> must be in <room>, <item_1> must have affordance unload, <item_1> has state loaded and open, <item_2> must have affordance pick and contained in <item_1>, <agent> has state hand-free. As result, <item_2> is in <room>, <item_1> changes from loaded to not-loaded, and <item_1> changes from open to closed."
          ]
        },
        "problems":
        {
            "problem_1": {
                  "description": "Baseline office setup task without events.",
                  "events": [],
                  "goal": "Set up a home office in the living room by bringing the lamp, locker and shelf along with their contents. Unload contents first, move each container to the living room, then reload the contents there. Note that you cannot move a loadable item if it is not empty!",
                  },
            "problem_2": {
                  "description": "The lamp was moved from its original location.",
                  "events": [
                    {
                      "time": EVENT_TIME_1,
                      "description": "Someone moved the lamp from closet to living_room."
                    }
                  ],
                  "goal": "Set up a home office in the living room by bringing the lamp, locker and shelf along with their contents. Unload contents first, move each container to the living room, then reload the contents there. Note that you cannot move a loadable item if it is not empty!. After setting up, put the lamp back where it originally was.",
                },
            "problem_3": {
                  "description": "The locker was opened before the task.",
                  "events": [
                    {
                      "time": EVENT_TIME_1,
                      "description": "Someone opened the locker in the bedroom."
                    }
                  ],
                  "goal": "Set up a home office in the living room by bringing the lamp, locker and shelf along with their contents. Unload contents first, move each container to the living room, then reload the contents there. Note that you cannot move a loadable item if it is not empty! After setting up, ensure the locker is in its original state.",
                },
            "problem_4": {
                  "description": "Multiple events: lamp moved several times before the task.",
                  "events": [
                    {
                      "time": EVENT_TIME_1,
                      "description": "Someone moved the lamp from closet to living_room."
                    },
                    {
                      "time": EVENT_TIME_2,
                      "description": "Someone moved the lamp from living_room to home_office."
                    }
                  ],
                  "goal": "Set up a home office in the living room by bringing the lamp, locker and shelf along with their contents. Unload contents first, move each container to the living room, then reload the contents there. Note that you cannot move a loadable item if it is not empty!. After setting up, put the lamp back before it was moved to the living_room.",
                }
        }
      },
      "pc":
      {
        "metadata":
        {
          "description": "Tasks related to assembling a PC.",
          "objects": ["agent", "room", "item","pc"],
          "actions":
          [
            "goto(<agent>, <room_1>, <room_2>): <agent> goes from <room_1> to <room_2>, where <room_1> and <room_2> should be neighbors. As result, <agent> will leave <room_1> and locates in <room_2>.",
            "pick(<agent>, <item>, <room>): <agent> picks up an <item> in <room>. <item> is accessible and located in <room>, <item> must have affordance pick.<agent> is in <room>, and <agent> state is hand-free. As result, <agent> has <item> in hand and <agent> state changes from hand-free to hand-busy.",
            "drop(<agent>, <item>, <room>): <agent> drops an <item> in <room>. <item> is accessible, <item> must have affordance drop, <agent> is in <room>, <agent> has <item> in hand, so <agent> state is hand-busy. As result, <item> will locate in <room>, <agent> no longer has <item> in hand, and <agent> state changes from hand-busy to hand-free.",
            "turnon(<agent>, <item>, <room>): <agent> turns on an <item> in <room>. <item> is accessible, <item> must have affordance turnon, both <agent> and <item> are in <room>, <agent> is hand-free, and <item> state is power_off. As result, <item> state changes from power_off to power_on.",
            "turnoff(<agent>, <item>, <room>): <agent> turns off an <item> in <room>. <item> is accessible, <item> must have affordance turnoff, both <agent> and <item> are in <room>, <agent> is hand-free, and <item> state is power_on. As result, <item> state changes from power_on to power_off.",
            "open(<agent>, <item>, <room>): <agent> opens an <item> in <room>. <item> is accessible, <item> must have affordance open, both <agent> and <item> are in <room>, <agent> is hand-free, and <item> state is closed. As result, <item> state changes from closed to open.",
            "close(<agent>, <item>, <room>): <agent> closes an <item> in <room>. <item> is accessible, <item> must have affordance close, both <agent> and <item> are in <room>, <agent> is hand-free,and <item> state is open. As result, <item> state changes from open to closed.",
            "assemble(<agent>, <room>, <item_1>, <item_2>, <item_3>, <item_4>, <item_5>, <item_6>, <pc>): a simplified action schema of assembling pc, the purpose of this action is to assemble a pc. <item_1> must be mainboard, <item_2> must be cpu, <item_3> must be ram, <item_4> must be ssd, <item_5> must be gpu, <item_6> must be psu, all items are accessible and have affordance pick. Before assemble, <pc> has not been assembled, <agent> and all <item>s should be in <room>, <agent> is hand-free and hold none of the <item>s in hand. As result, <pc> is assembled."
          ]
        },
        "problems":
        {
            "problem_1": {
                  "description": "Baseline PC assembly task without events.",
                  "events": [],
                  "goal": "Bring all necessary PC components (mainboard, cpu, ram, ssd, gpu, psu) to the living room and assemble pc.",
                  },
            "problem_2": {
                  "description": "One PC component was moved from its original location.",
                  "events": [
                    {
                      "time": EVENT_TIME_1,
                      "description": "Someone moved the ram from bedroom to living_room."
                    }
                  ],
                  "goal": "Bring all necessary PC components (mainboard, cpu, ram, ssd, gpu, psu) to the living room and assemble pc.",
                },
            "problem_3": {
                  "description": "A PC component was moved, and the assembly location depends on temporal query.",
                  "events": [
                    {
                      "time": EVENT_TIME_1,
                      "description": "Someone moved the ssd from living_room to kitchen."
                    }
                  ],
                  "goal": "Assemble pc in the room where the ssd was originally located. Bring all components there.",
                },
            "problem_4": {
                  "description": "Multiple PC components were moved before the task.",
                  "events": [
                    {
                      "time": EVENT_TIME_1,
                      "description": "Someone moved the mainboard from bedroom to living_room."
                    },
                    {
                      "time": EVENT_TIME_2,
                      "description": "Someone moved the cpu from home_office to kitchen."
                    }
                  ],
                  "goal": "Bring all necessary PC components (mainboard, cpu, ram, ssd, gpu, psu) to the living room and assemble pc.",
                }
        }
      }
    }
}
