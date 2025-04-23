import os
import cv2
import streamlit as st
from pytube import YouTube
import subprocess
from langchain_groq import ChatGroq
# Directories
videos_directory = 'videos/'
frames_directory = 'frames/'
os.makedirs (videos_directory, exist_ok=True)
os.makedirs (frames_directory, exist_ok=True)
