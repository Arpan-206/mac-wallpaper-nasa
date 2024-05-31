Steps to Have Live NASA Wallpaper on Your Desktop (MAC ONLY):

1. Create an API Key on [https://api.nasa.gov/](https://api.nasa.gov/)
2. Clone the repository
3. Install the dependencies using `pip install -r requirements.txt`
4. Make a `.env` file in the root directory and `NASA_TOKEN=YOUR_API_KEY` in it
5. Run the app using `python wallpaper-changer.py`
6. If you want to change the wallpaper every 12 hours, add the script to your crontab using `crontab -e` and add `0 */12 * * * <path-to-the-code>/wallpaper-changer.sh` to it
7. Enjoy your live NASA wallpaper!
# mac-wallpaper-nasa
