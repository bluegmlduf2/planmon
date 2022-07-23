from flask_restx import Resource
from flask import request,current_app,send_from_directory
from app.main.util import upload_image

from ..util.dto import ImageDto

api = ImageDto.api
_image = ImageDto.image


@api.route('/<status>/<param>')
@api.param('status', '임시이미지와 일반이미지구분')
@api.param('param', '이미지 파일명')
class Image(Resource):
    @api.doc('게시글 이미지 조회')
    def get(self,status,param):
        """게시물 이미지를 조회"""
        # 화면에서 저장한 이미지 
        fileName = param  # 요청URL에서 취득한 파일명
        
        # 이미지의 임시저장여부에 따라 다른 폴더경로에서 이미지를 가져온다
        if status =='temp':
            imageFilePath = current_app.config['POST_TEMP_FILE_PATH'] # 이미지파일 임시경로
        elif status == 'post':
            imageFilePath = current_app.config['POST_FILE_PATH'] # 이미지파일 경로

        # send_file()은 보안적으로 취약함
        return send_from_directory(imageFilePath, fileName)


@api.route('')
class ImageUpload(Resource):
    @api.doc('게시글 이미지 등록')
    @api.marshal_list_with(_image, envelope='data')
    def post(self):
        """게시물 이미지를 등록"""
        # 화면에서 저장한 이미지 
        file = request.files['image']
        
        # 파일이름 존재체크
        if file.filename == '':
            print('todo에러처리')

        # 빈파일체크
        if len(file.read()) == 0:
            print('todo에러처리')

        # 5MB 이상 업로드 방지
        if len(file.read()) > 5242880:
            print('todo에러처리')

        # 이미지 업로드
        url,filename = upload_image(file)

        return {'imagefileName':filename,'imageUrl': url}, 201