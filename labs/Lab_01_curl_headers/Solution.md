
## VSC
```shell
> GET / HTTP/2
> Host: code.visualstudio.com                                   - Значение хоста ресурса
> user-agent: curl/8.0.1                                        - Используемый браузер
> accept: */*
> 
< HTTP/2 200                                                    - Код ответа 200 "Запрос успешно обработан"
< content-length: 50213                                         - Размер отправляемого сообщения в байтах
< content-type: text/html; charset=utf-8                        - Формат данных
< accept-ranges: bytes
< etag: W/"c425-XBxswsHoV0dlJCAKuBbwZ9s5rjQ"                    - Идентификатор конкретной версии ресурса
< strict-transport-security: max-age=31536000; includeSubDomains
< content-security-policy: frame-ancestors 'self'               - Управляет ресурсами которые разрешено загружать user
< x-frame-options: SAMEORIGIN                                   - Указывает, следует ли разрешить браузеру отображать страницу
< x-xss-protection: 1; mode=block                               - Включает фильтрацию межсайтовых сценариев.
< x-content-type-options: nosniff                               - Отключает MIME
< x-content-type-options: nosniff
< x-powered-by: ASP.NET                                         - Может устанавливаться хостинговыми средами или другими   фреймворками и содержать инф о них
< x-azure-ref: 0z78CZQAAAAB5KdtNCSHMQaTxs7jdATjBU1RPRURHRTE0MTgAYmU4N2RjNmQtNDBmOS00NWIwLTg4MTAtOTkxMDg3ZWY4YjI5
< x-cache: CONFIG_NOCACHE
< date: Thu, 14 Sep 2023 08:09:51 GMT                            - Дата обращения
```

### RGUPS

```shell
Connected to www.rgups.ru (80.72.224.90) port 443 (#0) - Было описано ранее
using HTTP/1.x
GET / HTTP/1.1
Host: www.rgups.ru
User-Agent: curl/8.1.2
Accept: */*

HTTP/1.1 200 OK
Server: nginx/1.19.1
Date: Thu, 07 Sep 2023 09:31:21 GMT
Content-Type: text/html; charset=utf-8
Transfer-Encoding: chunked
Connection: keep-alive
X-Powered-By: ProcessWire CMS
Set-Cookie: wire=aee3aa42a2bbeff42e46de58ef8ce8a9; path=/; HttpOnly; SameSite=Lax
Expires: Thu, 19 Nov 1981 08:52:00 GMT                          - Дата/время, после которого ответ считается устаревшим.
Cache-Control: no-store, no-cache, must-revalidate              - Директивы для механизмов кэширования как в запросах, так и в ответах.
Pragma: no-cache                                                - Используется для обратной совместимости с кэшами HTTP/1.0
Vary: Accept-Encoding                                           - Определяет, как сопоставлять заголовки запросов
```

### Github

```shell
Connected to github.com (140.82.121.3) port 443 (#0)
using HTTP/1.x
GET / HTTP/1.1
Host: github.com
User-Agent: curl/8.1.2
Accept: */*

HTTP/1.1 200 OK
 Server: GitHub.com
 Date: Thu, 07 Sep 2023 09:35:10 GMT
 Content-Type: text/html; charset=utf-8
 Vary: X-PJAX, X-PJAX-Container, Turbo-Visit, Turbo-Frame, Accept-Language, Accept-Encoding, Accept, X-Requested-With
 content-language: en-US
 ETag: W/"f1f00e2684aaf25183523de15724ee1e"
 Cache-Control: max-age=0, private, must-revalidate
 Strict-Transport-Security: max-age=31536000; includeSubdomains; preload    - Принудительное подключение с использованием HTTPS вместо HTTP.
 X-Frame-Options: deny
 X-Content-Type-Options: nosniff
 X-XSS-Protection: 0

## Rgups

```shell
> GET / HTTP/1.1
> Host: www.rgups.ru
> User-Agent: curl/8.0.1
> Accept: */*
> 
< HTTP/1.1 200 OK
< Server: nginx/1.19.1
< Date: Thu, 14 Sep 2023 07:49:34 GMT
< Content-Type: text/html; charset=utf-8
< Transfer-Encoding: chunked
< Connection: keep-alive
< X-Powered-By: ProcessWire CMS
< Set-Cookie: wire=a542eba9537e9ffab0b8e7bcb77af417; path=/; HttpOnly; SameSite=Lax
< Expires: Thu, 19 Nov 1981 08:52:00 GMT                                    - Дата/время, после которого ответ считается устаревшим.
< Cache-Control: no-store, no-cache, must-revalidate
< Pragma: no-cache
< Vary: Accept-Encoding
```

## GitHub

```shell
> GET / HTTP/2
> Host: github.com
> user-agent: curl/8.0.1
> accept: */*
> 
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
* old SSL session ID is stale, removing
< HTTP/2 200 
< server: GitHub.com
< date: Thu, 14 Sep 2023 07:56:24 GMT
< content-type: text/html; charset=utf-8
< vary: X-PJAX, X-PJAX-Container, Turbo-Visit, Turbo-Frame, Accept-Language, Accept-Encoding, Accept, X-Requested-With
< content-language: en-US
< etag: W/"d268eab340b9cf22d0d14380cadfb115"
< cache-control: max-age=0, private, must-revalidate
< strict-transport-security: max-age=31536000; includeSubdomains; preload       - Принудительное подключение с использованием HTTPS вместо HTTP.
< x-frame-options: deny
< x-content-type-options: nosniff
< x-xss-protection: 0
< referrer-policy: origin-when-cross-origin, strict-origin-when-cross-origin
< content-security-policy: default-src 'none'; base-uri 'self'; child-src github.com/assets-cdn/worker/ gist.github.com/assets-cdn/worker/; connect-src 'self' uploads.github.com objects-origin.githubusercontent.com www.githubstatus.com collector.github.com raw.githubusercontent.com api.github.com github-cloud.s3.amazonaws.com github-production-repository-file-5c1aeb.s3.amazonaws.com github-production-upload-manifest-file-7fdce7.s3.amazonaws.com github-production-user-asset-6210df.s3.amazonaws.com cdn.optimizely.com logx.optimizely.com/v1/events *.actions.githubusercontent.com productionresultssa0.blob.core.windows.net/ productionresultssa1.blob.core.windows.net/ productionresultssa2.blob.core.windows.net/ productionresultssa3.blob.core.windows.net/ productionresultssa4.blob.core.windows.net/ productionresultssa5.blob.core.windows.net/ productionresultssa6.blob.core.windows.net/ productionresultssa7.blob.core.windows.net/ productionresultssa8.blob.core.windows.net/ productionresultssa9.blob.core.windows.net/ wss://*.actions.githubusercontent.com github-production-repository-image-32fea6.s3.amazonaws.com github-production-release-asset-2e65be.s3.amazonaws.com insights.github.com wss://alive.github.com github.githubassets.com; font-src github.githubassets.com; form-action 'self' github.com gist.github.com objects-origin.githubusercontent.com; frame-ancestors 'none'; frame-src viewscreen.githubusercontent.com notebooks.githubusercontent.com support.github.com; img-src 'self' data: github.githubassets.com media.githubusercontent.com camo.githubusercontent.com identicons.github.com avatars.githubusercontent.com github-cloud.s3.amazonaws.com objects.githubusercontent.com objects-origin.githubusercontent.com secured-user-images.githubusercontent.com/ user-images.githubusercontent.com/ private-user-images.githubusercontent.com opengraph.githubassets.com github-production-user-asset-6210df.s3.amazonaws.com customer-stories-feed.github.com spotlights-feed.github.com *.githubusercontent.com; manifest-src 'self'; media-src github.com user-images.githubusercontent.com/ secured-user-images.githubusercontent.com/ private-user-images.githubusercontent.com github.githubassets.com; script-src github.githubassets.com; style-src 'unsafe-inline' github.githubassets.com; upgrade-insecure-requests; worker-src github.com/assets-cdn/worker/ gist.github.com/assets-cdn/worker/
< set-cookie: _gh_sess=0Ixd%2BPoZibLWVYCxFlfAZ6C%2Ba78lVxhLk5cWFvGDUWm8et4DCkfx2yo4k1SWu1h5yWyLMjhs%2BCgkx%2B8BEGyF%2Fx1VYMVgODPWXsQTW5AqApPA0kd2xxk80%2FAf%2FCn4xNT2WWHIXqBPtRcKod4eGV5%2FRV%2BOZcErkOavaDqKm0A8M8LKyvYYnBzVchNcEcEGME%2B2eH8XyQ1gj3YHMT4MHzz1aTzM4L9r5UOHVuLlH9qCPB%2Fr2Xjm1aH%2Fq0iDI4U0JA8iT3xYrTF9Rz5wGf1QZCOXew%3D%3D--DD2Wci7fxw9at3LT--WUPGotCVr1I1vDlT3MiM2w%3D%3D; Path=/; HttpOnly; Secure; SameSite=Lax
< set-cookie: _octo=GH1.1.196778876.1694678185; Path=/; Domain=github.com; Expires=Sat, 14 Sep 2024 07:56:25 GMT; Secure; SameSite=Lax
< set-cookie: logged_in=no; Path=/; Domain=github.com; Expires=Sat, 14 Sep 2024 07:56:25 GMT; HttpOnly; Secure; SameSite=Lax
< accept-ranges: bytes
< x-github-request-id: 1B0E:0F0E:9ADA518:9CF4850:6502BCA9
< 
```

## RZD (don`t works)
```shell
> GET / HTTP/1.1
> Host: www.rzd.ru
> User-Agent: curl/8.0.1
> Accept: */*
> 
< HTTP/1.1 403 Forbidden
< Connection: close
< Content-Length: 109
< Content-Type: text/html
< 
* Closing connection 0
* TLSv1.2 (IN), TLS alert, close notify (256):
* TLSv1.2 (OUT), TLS alert, close notify (256):
```

# Yandex (don`t works)
```shell
> GET / HTTP/2
> Host: yandex.ru
> user-agent: curl/8.0.1
> accept: */*
> 
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
* old SSL session ID is stale, removing
< HTTP/2 302 
< location: https://dzen.ru/?yredirect=true
< date: Thu, 14 Sep 2023 08:02:26 GMT
< nel: {"report_to": "network-errors", "max_age": 100, "success_fraction": 0.001, "failure_fraction": 0.1}
< x-content-type-options: nosniff
< portal: Home
< set-cookie: is_gdpr=0; Path=/; Domain=.yandex.ru; Expires=Sat, 13 Sep 2025 08:02:26 GMT
< set-cookie: is_gdpr_b=COj6IhCrzgEoAg==; Path=/; Domain=.yandex.ru; Expires=Sat, 13 Sep 2025 08:02:26 GMT
< set-cookie: _yasc=0ZYqrHVyO4JVJx5CYp0GtihUnL/M4sVCRpm0kzW1ouHWkSGeakSBWHhLCqKZvIm4EQRA; domain=.yandex.ru; path=/; expires=Sun, 11 Sep 2033 08:02:26 GMT; secure
< set-cookie: i=KN41DXBHLWUeE7M97YI93Hd3t0OV/Vcczie4f4wjb2zOzJJTo7EtkxUeVV8b49VVxraYamVJUuR1/C8eV/Bxst9PVo8=; Expires=Sat, 13-Sep-2025 08:02:26 GMT; Domain=.yandex.ru; Path=/; Secure; HttpOnly
< set-cookie: yandexuid=3567004161694678546; Expires=Sat, 13-Sep-2025 08:02:26 GMT; Domain=.yandex.ru; Path=/; Secure
< p3p: policyref="/w3c/p3p.xml", CP="NON DSP ADM DEV PSD IVDo OUR IND STP PHY PRE NAV UNI"
< x-yandex-req-id: 1694678546304616-2376763490956700416-balancer-l7leveler-kubr-yp-sas-150-BAL-8661
< accept-ch: Sec-CH-UA-Platform-Version, Sec-CH-UA-Mobile, Sec-CH-UA-Model, Sec-CH-UA, Sec-CH-UA-Full-Version-List, Sec-CH-UA-WoW64, Sec-CH-UA-Arch, Sec-CH-UA-Bitness, Sec-CH-UA-Platform, Sec-CH-UA-Full-Version, Viewport-Width, DPR, Device-Memory, RTT, Downlink, ECT
< report-to: { "group": "network-errors", "max_age": 100, "endpoints": [{"url": "https://dr.yandex.net/nel", "priority": 1}, {"url": "https://dr2.yandex.net/nel", "priority": 2}]}
< cache-control: max-age=1209600,private
< x-robots-tag: unavailable_after: 12 Sep 2022 00:00:00 PST
< 
* Connection #0 to host yandex.ru left intact
```

## Python
```shell
> GET / HTTP/2
> Host: www.python.org
> user-agent: curl/8.0.1
> accept: */*
> 
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
< HTTP/2 200 
< server: nginx
< content-type: text/html; charset=utf-8
< x-frame-options: SAMEORIGIN
< via: 1.1 vegur, 1.1 varnish, 1.1 varnish
< accept-ranges: bytes
< date: Thu, 14 Sep 2023 08:05:26 GMT
< age: 1996
< x-served-by: cache-iad-kiad7000025-IAD, cache-fra-eddf8230106-FRA
< x-cache: HIT, HIT
< x-cache-hits: 9, 7
< x-timer: S1694678726.390360,VS0,VE0
< vary: Cookie
< strict-transport-security: max-age=63072000; includeSubDomains; preload
< content-length: 50214
```

## Saint git
```shell
> GET / HTTP/2
> Host: git-scm.com
> user-agent: curl/8.0.1
> accept: */*
> 
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
* old SSL session ID is stale, removing
< HTTP/2 200 
< date: Thu, 14 Sep 2023 08:07:36 GMT
< content-type: text/html; charset=utf-8
< x-frame-options: SAMEORIGIN
< x-xss-protection: 1; mode=block
< x-content-type-options: nosniff
< x-download-options: noopen
< x-permitted-cross-domain-policies: none
< referrer-policy: strict-origin-when-cross-origin
< cache-control: public, max-age=14400
< etag: W/"db69273d9410cbf4536e9d4b3a59685d"
< x-request-id: 5b655b2f-128f-4205-940e-13860b4aaf19
< x-runtime: 0.008824
< via: 1.1 vegur
< cf-cache-status: HIT
< age: 12785
< server: cloudflare
< cf-ray: 806723280e154c84-HEL
```

## Jetbrains
```shell
< HTTP/2 200 
< content-type: text/html; charset=utf-8
< content-length: 47213
< date: Thu, 14 Sep 2023 08:07:00 GMT
< server: nginx
< x-content-type-options: nosniff
< referrer-policy: same-origin
< expires: Thu, 14 Sep 2023 08:07:00 GMT
< cache-control: max-age=0
< pragma: no-cache
< x-frame-options: DENY
< x-content-type-options: nosniff
< x-xss-protection: 1; mode=block
< strict-transport-security: max-age=31536000;
< vary: Accept-Encoding
< via: 1.1 67b26e58a581719aff39a51e79faf096.cloudfront.net (CloudFront)
< alt-svc: h3=":443"; ma=86400
< age: 92
< set-cookie: cf_country-region=RU-ROS; Domain=jetbrains.com; Path=/; Secure
< x-cache: Hit from cloudfront
< x-amz-cf-pop: WAW51-P2
< x-amz-cf-id: K45sdod9RX_Vf9Cks3fZONvwYTYKGa_YcXolch6wEZ0LyQKY1QVkMA==
```
