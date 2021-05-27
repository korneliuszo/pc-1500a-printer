#!/bin/bash

AUDIOCARD=1
AUDIODEVICE=0
RMT_TTY="/dev/serial/by-id/usb-Silicon_Labs_CP2102_USB_to_UART_Bridge_Controller_0001-if00-port0"

amixer -c $AUDIOCARD sset "Mic" 0% off
amixer -c $AUDIOCARD sset "Speaker" 100%
amixer -c $AUDIOCARD sset "Auto Gain Control" on

stty -F $RMT_TTY raw
dd if=$RMT_TTY of=/dev/null bs=1 count=1
sleep 1
sox "$1" -t alsa hw:$AUDIOCARD,$AUDIODEVICE
