# -*- coding: utf-8 -*-
from dataapiclient import Client
if __name__ == "__main__":
    try:
        client = Client()
        client.init('24d3f9090c9ca88a79ac7d10bfa22fec410b3cd3f12c624e3e82f924621fc8ba')
        # url1='/api/macro/getChinaDataGDP.csv?field=&indicID=M010000002&indicName=&beginDate=&endDate='
        # code, result = client.getData(url1)
        # if code==200:
        #     print result
        # else:
        #     print code
        #     print result
        #
        # url2='/api/subject/getThemesContent.csv?field=&themeID=&themeName=&isMain=1&themeSource='
        # code, result = client.getData(url2)
        # if(code==200):
        #     file_object = open('thefile.csv', 'w')
        #     file_object.write(result)
        #     file_object.close( )
        # else:
        #     print code
        #     print result

        url3='/api/master/getSecID.json?field=&assetClass=&ticker=000001,600000&partyID=&cnSpell='
        code, result = client.getData(url3)
        if(code==200):
            print result
            # file_object = open('thefile.json', 'w')
            # file_object.write(result)
            # file_object.close( )
        else:
            print code
            print result
    except Exception, e:
        #traceback.print_exc()
        raise e