import http.client, urllib.request, urllib.parse, urllib.error, base64
import cognitive_face as cf
import FaceAPIConfig as cnfg
PERSON_Group_ID = 'autorizados_'
cf.BaseUrl.set (cnfg.facegroup_api_url)
cf.Key.set (cnfg.subscription_key)
#https://brazilsouth.api.cognitive.microsoft.com/face/v1.0/persongroups/autorizados_
subscription_key, face_api_url = cnfg.config();
name = "Lucas Diniz"
user_data = 'autorizado'
recognitionModel = 'recognition_02'
response = cf.person.create(PERSON_Group_ID,name,user_data)
person_id = response['personId']
#adicionando as imagens no grupo "autorizados_"
cf.person.add_face('imagens/imagem_PESONGROUP.jpeg', PERSON_Group_ID, person_id)
#mostrando no console as pessoas que estão adicionadas no grupo dos autorizadas
print (cf.person.lists(PERSON_Group_ID))
#sempre que adicionamos uma face nova é necessario treinar o modelo para melhorar a confiabilidade dos resultados
cf.person_group.train(PERSON_Group_ID,)
#resposta do retorno do treinamento do person group
response = cf.person_group.get_status(PERSON_Group_ID)
status = response['status']
#Verificando com outra foto se o inidividuo existe no grupo dos autorizados
response = cf.face.detect('imagens/fotocamera_AUTORIZADO.png',PERSON_Group_ID,recognitionModel)
face_ids = [d['faceId'] for d in response]
print (face_ids)
identified_faces = cf.face.identify( face_ids,PERSON_Group_ID,recognitionModel)
print (identified_faces)
# Identify faces
results = face_client.face.identify(face_ids, PERSON_GROUP_ID)
print('Identifying faces in {}'.format(cf.path.basename(image.name)))
if not results:
    print('ALERTA! Pessoa nao esta no grupo! nao foi autorizada')
for person in results:
    print('Pessoa para a id{} é identificada no grupo {} com um grau de confianca de {}.'.format(person.face_id, cf.path.basename(image.name), person.candidates[0].confidence))
        
