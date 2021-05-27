cmake_minimum_required(VERSION 3.10)
project(sharp-printer)

add_subdirectory(pocktool)

bas2img(
	BAS_FILE
		${CMAKE_CURRENT_SOURCE_DIR}/plot.bas
	IMG_FILE
		plot.img
	PC_TYPE
		1500
	)
img2wav(
	IMG_FILE
		plot.img
	WAV_FILE
		plot.wav
	PC_TYPE
		1500
	NAME
		PLOT
	TYPE
		img
	)
