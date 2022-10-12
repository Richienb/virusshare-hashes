import requests

print('Downloading…')

with open('virushashes.txt', 'w') as virushashes:
	isFirstLine = True

	for id in range(99999):
		url = f'https://virusshare.com/hashfiles/VirusShare_{str(id).zfill(5)}.md5'

		try:
			response = requests.get('https://virusshare.com/hashfiles/VirusShare_00000.md5', stream=True)
			response.encoding = 'utf-8'

			for line in response.iter_lines(decode_unicode=True):
				if line.startswith('#'):
					continue

				if isFirstLine:
					isFirstLine = False
				else:
					line = '\n' + line

				virushashes.write(line)

			print(f'Downloaded {url}')	
		except requests.exceptions.HTTPError as error:
			if error.response.status_code == 404:
				break

			raise error

print('Download complete')
