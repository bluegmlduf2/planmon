from flask_restx import Resource
from flask import request,current_app,send_from_directory
from app.main.util import upload_image,upload_user_image
from app.main.util.decorator import token_required
from app.main.service.auth_helper import Auth
from ..util.dto import ImageDto

api = ImageDto.api
_image = ImageDto.image


@api.route('/<status>/<param>')
@api.param('status', 'temp:임시이미지 post:일반이미지 userimage:유저이미지')
@api.param('param', '이미지 파일명')
class Image(Resource):
    @api.doc('이미지 조회')
    def get(self,status,param):
        """이미지를 조회"""
        # 화면에서 저장한 이미지 
        fileName = param  # 요청URL에서 취득한 파일명
        
        # 파라미터 구분자로 각 폴더경로에서 이미지를 가져온다
        if status =='temp':
            imageFilePath = current_app.config['POST_TEMP_FILE_PATH'] # 게시글 이미지파일 임시경로
        elif status == 'post':
            imageFilePath = current_app.config['POST_FILE_PATH'] # 게시글 이미지파일 경로
        elif status == 'userimage':
            imageFilePath = current_app.config['USER_FILE_PATH'] # 유저 이미지파일 경로

        # send_file()은 보안적으로 취약함
        return send_from_directory(imageFilePath, fileName)


@api.route('')
class ImageUpload(Resource):
    @token_required
    @api.doc('게시글 이미지 등록')
    @api.marshal_list_with(_image, envelope='data')
    def post(uid,self):
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


@api.route('/userimage')
class UserImageUpload(Resource):
    @token_required
    @api.doc('유저 이미지 등록')
    @api.marshal_list_with(_image, envelope='data')
    def post(uid,self):
        """유저 이미지를 등록"""
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
        url = upload_user_image(file)

        return {'imageUrl': url}, 201