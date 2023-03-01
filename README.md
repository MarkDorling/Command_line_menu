# Command_line_menu
<b>Command line menu system implemented using a dictionary data structure in Python.</b><br>
<br>
<i>This is an anonymised version of part of a project I did for a client in 2022.</i><br>
<br>
<b>Background:</b> My commissioning client requested an agile development process for their data science project, This included: data acquisition (scrapping and APIs), data wrangling, date storage (JSONs and MySQL) and visual representations (various plots and charts). As part of this project, for the client requested a command line-based navigation system to add and update, find and run scripts quickly and efficiently.<br>
<br>
<b>Problem:</b> The rapid development of new scripts required menus to be continually updated (adding, removing, and reordering menu items) leading to:<br>
• Continuity issues between menu options and associated functions;<br>
• Lengthy and inelegant code;<br>
• Duplication of menu related code;<br>
• Errors in program structure.<br>
<br>
<b>Client solution - Main:</b> I created a command line menu system underpinned by a dictionary data structure. The main menu, all sub-menus and menu items (menu option descriptions and associated function names) are stored in the dictionary. Please see the commented code for more details on how it works.<br>
<br>
<b>Generalised solution - Branch <i>( Generalised version with dynamic module names)</i>:</b> This is a generalised version of the main project that uses dynamic module names. In particular, the names of the dynamic module names (e.g. generic_tasks.py and generic_dictionary.py) are passed as arguments directly into the display_menu function within the interface.py; This allows this command line project to be used by anyone with their own dictionary and tasks py files. Furthermore, I also removed the selected_menu_number from the argument passed into the display_menu function within the interface.py; instead the variable is declared (with first number number) before the while loop; the selected_menu_number variable is updated within the loop as previously. <br>
<br>
<b>Config overview:</b><br>
• conda version : 23.1.0<br>
• conda-build version : 3.23.3<br>
• Python version : 3.9.16 <br>
• Requirements.txt <i>contains all library, packages and modules information</i>



