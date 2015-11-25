#!/usr/bin/env python
# -*- coding: utf8 -*-

import time

def fibonacci():
	ilksayi = 0
	ikincisayi = 1
	print ilksayi
	time.sleep(0.5)
	print ikincisayi
	time.sleep(0.5)
	while True:
		ilksayi = ilksayi + ikincisayi
		print ilksayi
		time.sleep(0.5)
		ikincisayi = ilksayi + ikincisayi
		print ikincisayi
		time.sleep(0.5)

fibonacci()