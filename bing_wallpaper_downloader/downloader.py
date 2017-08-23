#!/usr/bin/python

import requests


def getImageInfo():
    jsonUrl = 'http://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&nc=1503470814186&pid=hp&intlF=&quiz=1&fav=1'

    response = requests.get(jsonUrl)
    if response.status_code != 200:
        return

    try:
        rBody = response.json()
    except:
        print "Can not convert the response!"
        print response.content
        return

    return rBody['images'][0]


def getImage(imageUrl):
    response = requests.get(imageUrl)

    if response.status_code != 200:
        return

    imageData = response.content
    return imageData


def storeImage(imageData, imageName):
    storePath = ""
    with open(storePath + imageName, 'w+') as handler:
        handler.write(imageData)


def getImageUrl(imageInfo):
    siteStr = 'http://cn.bing.com'
    baseUrl = imageInfo['url']
    return siteStr + baseUrl

def getImageName(imageInfo):
    return imageInfo['enddate'] + '.jpg'

def main():
    info = getImageInfo()
    if info is None:
        print "get Image URL failed!"
        return

    url = getImageUrl(info)
    name = getImageName(info)

    data = getImage(url)
    if data is None:
        print "get Image failed!"
        return

    storeImage(data, name)


main()
