# config.py
'''Purpose: this module will let me access my database stored in this folder
'''
import os.path

package_dir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(package_dir, 'TVShows.db')
pic_path = os.path.join(package_dir, 'image.jpg')
