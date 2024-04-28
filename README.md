# spectaskular
Task management program that allows the set of display date, due date/time, and priority.

The newer versions of python should come with SQLite3 and Tkinter

The program does utilize tktimepicker  
pip install tkTimePicker

Pending tasks only display tasks in which
the display date is less than or equal to
the current date.
If you add a task with a display date that
is in the future it will not show up on
Pending tasks, but will show up on All tasks.
Likewise, if you have a task repeat, the display
time gets updated when completing the task, which
may cause a display time in the future thus dropping
the task off of Pending until that date comes.
The default display date is the current date.