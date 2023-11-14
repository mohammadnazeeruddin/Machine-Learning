{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3 5\n"
     ]
    }
   ],
   "source": [
    "class Point:\n",
    "    def __init__(self, x, y):\n",
    "        self.move(x, y)\n",
    "        \n",
    "\n",
    "    def move(self, x, y):\n",
    "        self.x = x\n",
    "        self.y = y\n",
    "\n",
    "    def reset(self):\n",
    "        self.move(5, 0)\n",
    "        print(\"this reset method calling move method\")\n",
    "\n",
    "# Constructing a Point\n",
    "point = Point(3, 5)\n",
    "print(point.x, point.y)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import sys\n",
    "from notebook import Notebook, Note\n",
    "\n",
    "class Menu:\n",
    "    '''Display a menu and respond to choices when run.'''\n",
    "    def __init__(self):\n",
    "        self.notebook = Notebook()\n",
    "        self.choices = {\n",
    "                \"1\": self.show_notes,\n",
    "                \"2\": self.search_notes,\n",
    "                \"3\": self.add_note,\n",
    "                \"4\": self.modify_note,\n",
    "                \"5\": self.quit\n",
    "                }\n",
    "\n",
    "    def display_menu(self):\n",
    "        print(\"\"\"\n",
    "Notebook Menu\n",
    "1. Show all Notes\n",
    "2. Search Notes\n",
    "3. Add Note\n",
    "4. Modify Note\n",
    "5. Quit\n",
    "\"\"\")\n",
    "\n",
    "    def run(self):\n",
    "        '''Display the menu and respond to choices.'''\n",
    "        while True:\n",
    "            self.display_menu()\n",
    "            choice = input(\"Enter an option: \")\n",
    "            action = self.choices.get(choice)\n",
    "            if action:\n",
    "                action()\n",
    "            else:\n",
    "                print(\"{0} is not a valid choice\".format(choice))\n",
    "\n",
    "    def show_notes(self, notes=None):\n",
    "        if not notes:\n",
    "            notes = self.notebook.notes\n",
    "        for note in notes:\n",
    "            print(\"{0}: {1}\\n{2}\".format(\n",
    "                note.id, note.tags, note.memo))\n",
    "\n",
    "    def search_notes(self):\n",
    "        filter = input(\"Search for: \")\n",
    "        notes = self.notebook.search(filter)\n",
    "        self.show_notes(notes)\n",
    "\n",
    "    def add_note(self):\n",
    "        memo = input(\"Enter a memo: \")\n",
    "        self.notebook.new_note(memo)\n",
    "        print(\"Your note has been added.\")\n",
    "\n",
    "    def modify_note(self):\n",
    "        id = input(\"Enter a note id: \")\n",
    "        memo = input(\"Enter a memo: \")\n",
    "        tags = input(\"Enter tags: \")\n",
    "        if memo:\n",
    "            self.notebook.modify_memo(id, memo)\n",
    "        if tags:\n",
    "            self.notebook.modify_tags(id, tags)\n",
    "\n",
    "    def quit(self):\n",
    "        print(\"Thank you for using your notebook today.\")\n",
    "        sys.exit(0)\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    Menu().run()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
