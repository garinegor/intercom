import cognitive_face as CF

KEY = '3c064f7a007c4ce2834f49aa740bcc42'
CF.Key.set(KEY)
CF.BaseUrl.set('https://westcentralus.api.cognitive.microsoft.com/face/v1.0/')

faces={'george':['8cb744fc-734d-48c2-8633-af34f3d5ff4e', 'dea5a71e-a2ae-4da3-be2c-2518cc2c8122', 'ac964b92-cbfe-413b-bfae-685c3ac48ae3', 'fa69dadf-1bf9-407c-b4e2-4edb8273d51c']}

# faces = CF.face.detect(input())
# print(faces)

def compare(name,path):
	to_r=False
	faces_result = CF.face.detect(path)
	if len(faces_result)==1:
		new_face=faces_result[0]['faceId']
		result=CF.face.group(faces[name]+[new_face])
		if new_face in result['groups'][0]:
			to_r=True
	return to_r

print(compare('george','./images/image4.jpg'))