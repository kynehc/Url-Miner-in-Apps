# Url-Analysis-in-Apps

this project using this android analysis library [Androiguard](https://github.com/androguard/androguard)

`pip install -U androguard`

## For url analysis in apps

test apps in /apk

results log in /result

test.sh for running python on all apks in /apk

## runing example

`python url.py apk/com.edaixi.apk`

```
start at:2020-06-03 16:37:38.312555

[*] Analyzing APK ...

[*]url patern found:
FOUND: 1 http://payment.edaixi.com/payment/baidu_delivery
XREFto for string 'http://payment.edaixi.com/payment/baidu_delivery' in
Lcom/edaixi/pay/bdpay/BDPayCore;:Lcom/edaixi/pay/bdpay/BDPayCore;->createOrderInfo(Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Ljava/lang/String;)Ljava/lang/String; [access_flags=private] @ 0x388e84

FOUND: 2 http://payment.edaixi.com/payment/wechat_delivery_notify
XREFto for string 'http://payment.edaixi.com/payment/wechat_delivery_notify' in
Lcom/edaixi/pay/wechatpay/WeChatPayCore;:Lcom/edaixi/pay/wechatpay/WeChatPayCore;->genProductArgs()Ljava/lang/String; [access_flags=private] @ 0x38a10c

FOUND: 3 http://payment.edaixi.com/payment/baidu_delivery
XREFto for string 'http://payment.edaixi.com/payment/baidu_delivery' in
Lcom/edaixi/pay/bdpay/BDPayCore;:Lcom/edaixi/pay/bdpay/BDPayCore;->createOrderInfo(Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Ljava/lang/String;)Ljava/lang/String; [access_flags=private] @ 0x388e84

FOUND: 4 http://payment.edaixi.com/payment/wechat_delivery_notify
XREFto for string 'http://payment.edaixi.com/payment/wechat_delivery_notify' in
Lcom/edaixi/pay/wechatpay/WeChatPayCore;:Lcom/edaixi/pay/wechatpay/WeChatPayCore;->genProductArgs()Ljava/lang/String; [access_flags=private] @ 0x38a10c


[*]url class path found:
FOUND: 5 http://secclientgw.alipay.com/mobile/switch.xml
XREFto for string 'http://secclientgw.alipay.com/mobile/switch.xml' in
Lcom/alipay/mobilesecuritysdk/model/Upload;:Lcom/alipay/mobilesecuritysdk/model/Upload;->communicateSwitch()Lcom/alipay/mobilesecuritysdk/datainfo/GeoResponseInfo; [access_flags=public] @ 0x218a68

FOUND: 6 http://m.alipay.com/?action=h5quit
XREFto for string 'http://m.alipay.com/?action=h5quit' in
Lcom/alipay/sdk/app/H5PayActivity$MyWebViewClient;:Lcom/alipay/sdk/app/H5PayActivity$MyWebViewClient;->shouldOverrideUrlLoading(Landroid/webkit/WebView; Ljava/lang/String;)Z [access_flags=public] @ 0x21aed4
Lcom/alipay/sdk/app/H5AuthActivity$MyWebViewClient;:Lcom/alipay/sdk/app/H5AuthActivity$MyWebViewClient;->shouldOverrideUrlLoading(Landroid/webkit/WebView; Ljava/lang/String;)Z [access_flags=public] @ 0x219c4c

FOUND: 7 http://mcashier.stable.alipay.net/home/exterfaceAssign.htm?
XREFto for string 'http://mcashier.stable.alipay.net/home/exterfaceAssign.htm?' in
Lcom/alipay/sdk/app/PayTask;:Lcom/alipay/sdk/app/PayTask;->b()Ljava/lang/String; [access_flags=private] @ 0x21c3c4
Lcom/alipay/sdk/app/PayTask;:Lcom/alipay/sdk/app/PayTask;->a()Ljava/lang/String; [access_flags=private] @ 0x21bfac

FOUND: 8 http://mobileclientgw.stable.alipay.net/home/exterfaceAssign.htm?
XREFto for string 'http://mobileclientgw.stable.alipay.net/home/exterfaceAssign.htm?' in
Lcom/alipay/sdk/app/PayTask;:Lcom/alipay/sdk/app/PayTask;->b()Ljava/lang/String; [access_flags=private] @ 0x21c3c4
Lcom/alipay/sdk/app/PayTask;:Lcom/alipay/sdk/app/PayTask;->a()Ljava/lang/String; [access_flags=private] @ 0x21bfac

FOUND: 9 http://mcgw.alipay.com/gateway.do
XREFto for string 'http://mcgw.alipay.com/gateway.do' in
Lcom/alipay/sdk/cons/GlobalConstants;:Lcom/alipay/sdk/cons/GlobalConstants;-><clinit>()V [access_flags=static constructor] @ 0x21eeec

FOUND: 10 http://co.baifubao.com/content/mywallet/mobile/score_tip.cfg
XREFto for string 'http://co.baifubao.com/content/mywallet/mobile/score_tip.cfg' in
Lcom/baidu/paysdk/beans/e;:Lcom/baidu/paysdk/beans/e;->getUrl()Ljava/lang/String; [access_flags=public] @ 0x2aa740

FOUND: 11 http://www.baidu.com
XREFto for string 'http://www.baidu.com' in
Lcom/baidu/paysdk/login/LoginActivity;:Lcom/baidu/paysdk/login/LoginActivity;->buildUrl(I)Ljava/lang/String; [access_flags=private] @ 0x2b1054
Lcom/baidu/paysdk/login/LoginActivity$CustWebViewClient;:Lcom/baidu/paysdk/login/LoginActivity$CustWebViewClient;->onPageStarted(Landroid/webkit/WebView; Ljava/lang/String; Landroid/graphics/Bitmap;)V [access_flags=public] @ 0x2afec4

FOUND: 12 http://co.baifubao.com/content/resource/HTML5/eptos.html
XREFto for string 'http://co.baifubao.com/content/resource/HTML5/eptos.html' in
Lcom/baidu/paysdk/ui/WebViewActivity;:Lcom/baidu/paysdk/ui/WebViewActivity;->onCreate(Landroid/os/Bundle;)V [access_flags=public] @ 0x2c38ec

FOUND: 13 http://payment.edaixi.com/payment/baidu_delivery
XREFto for string 'http://payment.edaixi.com/payment/baidu_delivery' in
Lcom/edaixi/pay/bdpay/BDPayCore;:Lcom/edaixi/pay/bdpay/BDPayCore;->createOrderInfo(Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Ljava/lang/String;)Ljava/lang/String; [access_flags=private] @ 0x388e84

FOUND: 14 http://payment.edaixi.com/payment/wechat_delivery_notify
XREFto for string 'http://payment.edaixi.com/payment/wechat_delivery_notify' in
Lcom/edaixi/pay/wechatpay/WeChatPayCore;:Lcom/edaixi/pay/wechatpay/WeChatPayCore;->genProductArgs()Ljava/lang/String; [access_flags=private] @ 0x38a10c

Total Found: 14

end at:2020-06-03 16:38:07.291726
total time:0:00:28.979171
Maximum Memory Usage: 879.22265625 MB
```
