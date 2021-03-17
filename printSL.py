import requests

resp = requests.get("https://www.shiftleft.io/api/v4/orgs/592bbe22-3def-4eb5-b468-3ed72735a24b/apps/vulnado/findings?severity=critical", headers={"Authorization":"Bearer eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2MTU1OTA3MDMsImlzcyI6IlNoaWZ0TGVmdCIsIm9yZ0lEIjoiNTkyYmJlMjItM2RlZi00ZWI1LWI0NjgtM2VkNzI3MzVhMjRiIiwidXNlcklEIjoiZjQ0YjEyMmQtZjBjZS00NzcyLThhYWEtZmYzYTQyMTVkYjc4Iiwic2NvcGVzIjpbInNlYXRzOndyaXRlIiwiZXh0ZW5kZWQiLCJhcGk6djIiLCJ1cGxvYWRzOndyaXRlIiwibG9nOndyaXRlIiwicGlwZWxpbmVzdGF0dXM6cmVhZCIsIm1ldHJpY3M6d3JpdGUiLCJwb2xpY2llczpjdXN0b21lciJdfQ.cEmtz9Re4BNaB1eAxa8dDJkXdXKqaO1SfldX6NkfYy6BcyRw6EGEbazCJq8CCR9rR-y3hb7cqllq2eTDiCf-v_udairBuBAczSD5BHFgQ2P2awUFb9xBfw3O68fEVbBmhds-ErPgJ394fA9assdmzpxjTRGQwGQChQod0biPEli-3NN2SpHeQfJjt-5y3TNHtRjJdYraobCfRiRTQyP5Yyj5f97PHSZ-MnYAEhfrsoBC1aNgZSCIP_gz4k-SNP2_YrFX09tURK_AX83jR90P1V-9FnlNGAfTUDPe5oXcWcq7sPMvNNFW6JAqpSFkFqDWEGkw17B5s3krQlNqYkhkUg"})

findings = resp.json()['response']['findings']
print("========== ShiftLeft found the following critical vulnerabilities ==========")
for v in findings:
	print("ID: "+ v['id'] + "\nTitle: " + v['title'])
print("============================================================================")
