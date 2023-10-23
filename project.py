import streamlit as st
import os
import webbrowser
try:
    from ctypes import cast, POINTER
    from comtypes import CLSCTX_ALL
    from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

    # Define functions that use comtypes
    def increase_volume():
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        a = volume.GetMasterVolumeLevel()
        volume.SetMasterVolumeLevel(a + 10.0, None)

        st.success("Volume increased.")

    def decrease_volume():
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        a = volume.GetMasterVolumeLevel()
        volume.SetMasterVolumeLevel(a - 10.0, None)

        st.success("Volume decreased.")

except ImportError:
    st.warning("Volume control functions are not available on this platform.")

def open_folder(folder_name):
    common_folders = ["downloads", "documents", "desktop"]
    
    folder_name_lower = folder_name.lower()
    
    for folder in common_folders:
        if folder_name_lower in folder:
            folder_path = os.path.join(os.path.expanduser("~"), folder)
            os.startfile(folder_path)
            st.success(f"Opened folder: {folder_path}")
            return

    st.error(f"Folder '{folder_name}' not found.")

def play_music(song, artist):
    search_song = f"https://www.audiomack.com/{artist}/song/{song}"
    webbrowser.open(search_song)
    st.success(f"Searching for: {song} by {artist}")

def search_google(query):
    search_url = f"https://www.google.com/search?q={query}"
    webbrowser.open(search_url)
    st.success(f"Searching Google for: {query}")

def main():
    st.set_page_config(
        page_title="Remote Desktop Control",
        page_icon=":computer:",
        layout="wide"
    )

    # Dark blue theme
    st.markdown(
        """
        <style>
       
        .st-bq {
            color: white;
        }
         body {
            color: white;
            background-color: #001F3F;
        }
        .st-bb {
            background-color: #001F3F;
        }
        .st-c1 {
            color: #0074e4;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("Remote Desktop Control")
    st.write("Welcome to the Remote Desktop Control app! Use the buttons below to perform various functions.")

    function_choice = st.selectbox("Select Function", ["Open Folder", "Increase Volume", "Decrease Volume", "Search Google", "Play Music"])

    if function_choice == "Open Folder":
        folder_name = st.text_input("Enter Folder Name")
        if st.button("Open Folder"):
            open_folder(folder_name)

    elif function_choice == "Increase Volume":
        if st.button("Increase Volume"):
            increase_volume()

    elif function_choice == "Decrease Volume":
        if st.button("Decrease Volume"):
            decrease_volume()

    elif function_choice == "Search Google":
        query = st.text_input("Enter Search Query")
        if st.button("Search Google"):
            search_google(query)

    elif function_choice == "Play Music":
        song = st.text_input("Enter Song Name")
        artist = st.text_input("Enter Artist Name")
        if st.button("Play Music"):
            play_music(song, artist)

if __name__ == "__main__":
    main()

