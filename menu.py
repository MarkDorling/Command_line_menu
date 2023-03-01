""" The dictionary data structure storing all the menu related data """

dict_menu = {1 : {'title': 'Main Menu',
                      'format' : '1',
                      'instruction': 'Main Menu description here...',
                      'table': {'0': ['Exit', 'exit_menu'],
                                '1': ['Load Sub-Menu 1 (Get Data)', 'menu_2'],
                                '2': ['Load Sub-Menu 2 (Wrangling / Storing)', 'menu_3'],
                                '3': ['Load Sub-Menu 3 (Reporting / Exporting)', 'menu_4']
                                }
                  },
             2 : {'title': 'Sub-Menu 1 (Get data)',
                      'format' : '2',
                      'instruction': 'Sub-Menu 1 (Get Data) description here... ',
                      'table': {'0': ['Return to Main Menu', 'menu_1'],
                                '1': ['Load Web Scrappping Task', 'scrape_task'],
                                '2': ['Load Json Input Task', 'import_json_task']
                                }
                 },
             3 : {'title': 'Sub-Menu 2 (Wrangling / Storing)',
                      'format' : '3',
                      'instruction': 'Sub-Menu 2 (Wrangling / Storing) description... ',
                      'table': {'0': ['Return to Main Menu', 'menu_1'],
                                '1': ['Load Wrangling Task', 'wrangle_task'],
                                '2': ['Load Storing Task', 'store_task']
                                }
                 },
             4 : {'title': 'Sub-Menu 3 (Reporting / Exporting)',
                     'format' : '3',
                     'instruction': 'Sub-Menu 3 (Reporting / Exporting) description... ',
                     'table': {'0': ['Return to Main Menu', 'menu_1'],
                               '1': ['Load Json Export Task', 'export_json_task'],
                               '2': ['Load Data Plotting Task', 'plot_task']
                              }
                 }
            }


