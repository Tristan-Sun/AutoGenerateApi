AutoGenerationApis/apis.properties                                                                  000644  001751  001751  00000013071 11727616457 021127  0                                                                                                    ustar 00tristan                         tristan                         000000  000000                                                                                                                                                                         # clent
client.login=ClientLoginRequest,LoginResponse
client.getLoginInfo=ClientGetLoginInfoRequest,LoginResponse

# feed
#v.feed.get
feed.get=FeedGetRequest,FeedGetResponse
feed.read=FeedReadRequest,SubmitResponse
feed.publishFeed=FeedPublishFeedRequest,SubmitResponse

# video
video.get=VideoGetRequest,VideoGetResponse
video.getUrl=VideoGetUrlRequest,VideoUploadeUrl
video.save=VideoSaveRequest,SubmitResponse

# share
share.getComments=ShareGetCommentsRequest,ShareCommentListResponse
share.addComment=ShareAddCommentRequest,SubmitResponse
share.getHots=ShareGetHotsRequest,ShareGetsResponse
share.gets=ShareGetsRequest,ShareGetsResponse
share.get=ShareGetRequest,ShareItemResponse
share.publish=SharePublishRequest,SubmitResponse
share.delete=ShareDeleteRequest,SubmitResponse
share.publishLink=SharePublishLinkRequest,SubmitResponse
share.getLink=ShareGetLinkRequest,ShareGetLinkResponse

# blog
blog.gets=GetsBlogRequest,BlogListResponse
blog.get=GetBlogRequest,BlogResponse
blog.add=AddBlogRequest,BlogAddResultResponse
blog.delete=DeleteBlogRequest,SubmitResponse
blog.deleteComment=DeleteBlogCommentRequest,SubmitResponse
blog.getCategory=GetBlogCategoryRequest,BlogCategoryListResponse
blog.getComments=GetBlogCommentsRequest,BlogCommentResponse
blog.addComment=AddBlogCommentRequest,SubmitResponse
blog.privacy=BlogPrivacyRequest,PrivacyResponse

# gossip
gossip.postGossip=GossipPostGossipRequest,SubmitResponse
gossip.gets=GossipGetsRequest,GossipListResponse
gossip.delete=GossipDeleteRequest,SubmitResponse

# friends
friends.getFriends=FriendsGetFriendsRequest,MyFriendsListResponse
friends.getOnlineFriends=FriendsGetOnlineFriendsRequest,MyFriendsListResponse
friends.isOnline=FriendsIsOnlineRequest,MyFriendsListResponse
friends.search=FriendsSearchRequest,FriendsSearchResponse
friends.getSharedFriends=FriendsGetSharedFriendsRequest,FriendsSharedResponse
friends.areFriends=FriendsAreFriendsRequest,FriendInfoListResponse
friends.request=FriendsRequestRequest,SubmitResponse
friends.accept=FriendsAcceptRequest,SubmitResponse
friends.getRequests=FriendsGetRequestsRequest,FriendApplyListResponse
friends.denyAll=FriendsDenyAllRequest,SubmitResponse
friends.deny=FriendsDenyRequest,SubmitResponse
friends.recommend=FriendsRecommendRequest,FriendsSearchResponse
friends.removeFriend=FriendsRemoveFriendRequest,SubmitResponse
friends.addFocusFriend=FriendsAddFocusFriendRequest,SubmitResponse
friends.delFocusFriend=FriendsDelFocusFriendRequest,SubmitResponse
friends.getFocusFriends=FriendsGetFocusFriendsRequest,MyFriendsListResponse

# news
news.getCount=NewsGetCountRequest,NewsTotalResponse
news.getClientCount=NewsGetClientCountRequest,NewsTotalResponse
news.push=NewsPushRequest,NewsListResponse
news.newsList=NewsNewsListRequest,NewsListResponse
news.friendRequestList=NewsFriendRequestListRequest,NewsListResponse
news.readNewsById=NewsReadNewsByIdRequest,SubmitResponse
news.readNewsBySourceId=NewsReadNewsBySourceIdRequest,SubmitResponse
news.getFriendsBirthdayList=NewsGetFriendsBirthdayListRequest,FriendBirthDayListResponse

# photos
#photos.upload
#photos.uploadbin
#photos.uploadHead
#photos.uploadCover
photos.sendFeed=PhotosSendFeedRequest,SubmitResponse
photos.getAlbums=PhotosGetAlbumsRequest,AlbumListResponse
photos.get=PhotosGetRequest,PhotoListResponse
photos.getCover=PhotosGetCoverRequest,PhotosCoverResponse
photos.getNewUploaded=PhotosGetNewUploadedRequest,PhotoListResponse
photos.getComments=PhotosGetCommentsRequest,PhotoCommentListResponse
photos.addComment=PhotosAddCommentRequest,SubmitResponse
photos.deleteComment=PhotosDeleteCommentRequest,SubmitResponse
photos.createAlbum=PhotosCreateAlbumRequest,AlbumCreateResponse
photos.delete=PhotosDeleteRequest,SubmitResponse
photos.edit=PhotosEditRequest,SubmitResponse
photos.privacy=PhotosPrivacyRequest,PrivacyResponse
photos.addTags=PhotosAddTagRequest,SubmitResponse
photos.getTags=PhotosGetTagsRequest,PhotoTagListResponse
photos.deleteTag=PhotosDeleteTagRequest,SubmitResponse
photos.deleteTagAll=PhotosDeleteTagAllRequest,SubmitResponse

# status
status.set=StatusSetRequest,SubmitResponse
status.forward=StatusForwardRequest,SubmitResponse
status.get=StatusGetRequest,DoingResponse
status.gets=StatusGetsRequest,DoingListResponse
status.getLast=StatusGetLastRequest,LastDoingListResponse
status.addComment=StatusAddCommentRequest,SubmitResponse
status.getComments=StatusGetCommentsRequest,DoingCommentListResponse
status.remove=StatusRemoveRequest,SubmitResponse
status.removeComment=StatusRemoveCommentRequest,SubmitResponse
status.getEmoticons=StatusGetEmoticonsRequest,EmoticonListResponse

# page
page.isPage=PageIsPageRequest,SubmitResponse
page.isFans=PageIsFansRequest,SubmitResponse
page.becomeFan=PageBecomeFanRequest,SubmitResponse
page.quitFans=PageQuitFansRequest,SubmitResponse
page.getList=PageGetListRequest,PageListResponse
page.getFansList=PageGetFansListRequest,FansListResponse
page.getInfo=PageGetInfoRequest,PageInfoResponse
page.search=PageSearchRequest,PageListResponse

# phoneclient
phoneclient.getUpdateInfo=PhoneclientGetUpdateInfoRequest,UpdateInfoResponse
phoneclient.activeClient=PhoneclientActiveClientRequest,SubmitResponse
phoneclient.actionLog=PhoneclientActionLogRequest,SubmitResponse
phoneclient.sdkLog=PhoneclientSdkLogRequest,SubmitResponse
phoneclient.getErrorMsg=PhoneclientGetErrorMsgRequest,PhoneClientGetErrorMsgResponse
phoneclient.toolLog=PhoneclientToolLogRequest,SubmitResponse
phoneclient.getRegexMsg=PhoneclientGetRegexMsgRequest,PhoneClientGetRegexMsgResponse

# push
push.addToken=PushAddTokenRequest,SubmitResponse
push.addWin8Token=PushAddWin8TokenRequest,SubmitResponse

# batch.run
batch.run=BatchRunRequest,BatchRunResponse

                                                                                                                                                                                                                                                                                                                                                                                                                                                                       AutoGenerationApis/autoGeneration.py                                                                000755  001751  001751  00000034405 11726350500 021401  0                                                                                                    ustar 00tristan                         tristan                         000000  000000                                                                                                                                                                         #! /usr/local/bin/python

import re
import os

DEBUG = True
RESPONSE_FILE = "responses.proto"
REQUEST_FILE = "requests.proto"
APIS_FILE = "apis.properties"

TYPES = {"int32":"int", "int64":"long", "string":"String", "float":"float", "double":"double", "bool":"boolean"}
PROPERTIES = ("required", "optional", "repeated")

PACKAGE_PREFIX = "com.renren.mobile.rmsdk"

def log(message):
    if DEBUG:
        print message

class Field:
    def __init__(self):
        self.name = None
        self.type = None
        self.property = None
        self.default = None
        self.order = None

    def getRealType(self):
        realType = self.type
        if TYPES.has_key(realType):
            realType = TYPES.get(realType)
        if PROPERTIES[2] == self.property:
            realType += "[]"
        return realType

    def getRealName(self):
        return self.changeUnderlineToHump(self.name)

    def getFieldDeclaration(self, indentation):
        prefix = '\t' * indentation
        content = list()
        content.append("%sprivate %s %s" % (prefix, self.getRealType(), self.getRealName()))
        if not self.default == None:
            content.append(" = %s" % self.default)
        content.append(";\n")
        content.append("\n")
        return ''.join(content)

    def getFieldJsonProperty(self, indentation):
        prefix = '\t' * indentation
        return '%s@JsonProperty("%s")\n' % (prefix, self.name)

    def getFieldRequiredOrOptional(self, indentation):
        prefix = '\t' * indentation
        if self.property == PROPERTIES[0]:
            return '%s@RequiredParam("%s")\n' % (prefix, self.name)
        elif self.property == PROPERTIES[1]:
            return '%s@OptionalParam("%s")\n' % (prefix, self.name)

    def getSetterMethod(self, indentation):
        content = list()
        prefix = '\t' * indentation
        realName = self.getRealName()
        methodName = realName[0].capitalize() + realName[1:]
        realType = self.getRealType()
        content.append("%spublic void set%s(%s %s) {\n" % (prefix, methodName, realType, realName))
        content.append("%s\tthis.%s = %s;\n" %(prefix, realName, realName))
        content.append("%s}\n" % prefix)
        content.append("\n")
        return ''.join(content)

    def getGetterMethod(self, indentation):
        content = list()
        prefix = '\t' * indentation
        realName = self.getRealName()
        methodName = realName[0].capitalize() + realName[1:]
        realType = self.getRealType()
        content.append("%spublic %s get%s() {\n" % (prefix, realType, methodName))
        content.append("%s\treturn this.%s;\n" %(prefix, realName))
        content.append("%s}\n" % prefix)
        content.append("\n")
        return ''.join(content)

    # Change naming style from underline to hump.
    def changeUnderlineToHump (self, underlineName):
        result = "".join([word.capitalize() for word in underlineName.split("_")])
        return result[0].lower() + result[1:]

class Response:
    definedInnerClasses = list()

    def __init__(self):
        self.restMethodName = None
        self.fields = list()

    def getInnerClasses(self):
        innerClasses = list()
        for field in self.fields:
            if not TYPES.has_key(field.type):
                innerClasses.append(field.type)
        # Save all inner classes corresponding to the top level response. Avoid endless recursion.
        Response.definedInnerClasses.extend(innerClasses)
        return innerClasses

    def generateInnerClass(self, innerClassName, indentation, responses):
        prefix = '\t' * indentation
        content = list()
        content.append("%spublic static class %s {\n" % (prefix, innerClassName))
        for field in self.fields:
            content.append(field.getFieldJsonProperty(indentation + 1))
            content.append(field.getFieldDeclaration(indentation + 1))
        for field in self.fields:
            content.append(field.getSetterMethod(indentation + 1))
            content.append(field.getGetterMethod(indentation + 1))
        innerClasses = self.getInnerClasses()
        for responseName in innerClasses:
            # If the inner class is already defined, then we don't define again, to avoid endless loop.
            if Response.definedInnerClasses.count(responseName) == 0:
                # Recursion
                content.append(responses[responseName].generateInnerClass(responseName, indentation + 1, responses))
        content.append("%s}\n" % prefix)
        content.append("\n")
        return ''.join(content)

    def generateJavaSource(self, responses):
        if self.restMethodName == None or len(self.fields) == 0:
            return

        packageName, className = self.restMethodName.split('.')
        classNamePrefix = packageName.capitalize() + className[0].capitalize() + className[1:]
        log("Generating %s.%s.%sResponse.java ..." % (PACKAGE_PREFIX, packageName, classNamePrefix))

        fileDir = "./src/%s/%s" % (PACKAGE_PREFIX.replace(".", "/"), packageName)
        if not os.path.exists(fileDir):
            os.makedirs(fileDir)
        f = open("%s/%sResponse.java" % (fileDir, classNamePrefix) ,"w")
        content = list()
        # write package line
        content.append("package %s.%s;\n" % (PACKAGE_PREFIX, packageName))
        content.append("\n")
        # write import lines
        content.append("import com.renren.mobile.rmsdk.core.base.ResponseBase;\n")
        content.append("import com.renren.mobile.rmsdk.core.json.JsonProperty;\n")
        content.append("\n")
        # class name
        content.append("public class %sResponse extends ResponseBase {\n" % classNamePrefix)
        # properties declaration
        indentation = 1
        for field in self.fields:
            content.append(field.getFieldJsonProperty(indentation))
            content.append(field.getFieldDeclaration(indentation))

        # methods declaration
        for field in self.fields:
            # get method
            content.append(field.getGetterMethod(indentation))
            # set method
            content.append(field.getSetterMethod(indentation))

        # our custom inner classes
        for innerClassName in self.getInnerClasses():
            content.append(responses[innerClassName].generateInnerClass(innerClassName, indentation, responses))

        content.append("}\n")

        # when this response's source code was finished, we should clear Response.definedInnerClasses
        Response.definedInnerClasses = list()

        f.write(''.join(content))
        f.close()

class Request:
    def __init__(self):
        self.needSessionKey = -1
        self.restMethodName = None
        self.fields = list()

    def insertField(self, field):
        if field.name == "session_key":
            if field.property == PROPERTIES[0]:
                self.needSessionKey = 1
            elif field.property == PROPERTIES[1]:
                self.needSessionKey = 0
        else:
            self.fields.append(field)

    def hasOptionalParam(self):
        for field in self.fields:
            if field.property == PROPERTIES[1]:
                return True
        return False

    def hasRequiredParam(self):
        for field in self.fields:
            if field.property == PROPERTIES[0]:
                return True
        return False

    def getRequiredParams(self):
        requiredParams = list()
        for field in self.fields:
            if field.property == PROPERTIES[0]:
                requiredParams.append(field)
        return requiredParams

    def getOptionalParams(self):
        optionalParams = list()
        for field in self.fields:
            if field.property == PROPERTIES[1]:
                optionalParams.append(field)
        return optionalParams


    def generateJavaSource(self):
        if self.restMethodName == None:
            return

        packageName, className = self.restMethodName.split('.')
        classNamePrefix = packageName.capitalize() + className[0].capitalize() + className[1:]

        log("Generating %s.%s.%sRequest.java ..." % (PACKAGE_PREFIX, packageName, classNamePrefix))

        fileDir = "./src/%s/%s" % (PACKAGE_PREFIX.replace(".", "/"), packageName)
        if not os.path.exists(fileDir):
            os.makedirs(fileDir)
        f = open("%s/%sRequest.java" % (fileDir, classNamePrefix) ,"w")
        content = list()
        # write package line
        content.append("package %s.%s;\n" % (PACKAGE_PREFIX, packageName))
        content.append("\n")
        # write import lines
        content.append("import com.renren.mobile.rmsdk.core.base.RequestBase;\n")
        content.append("import com.renren.mobile.rmsdk.core.annotations.RestMethodName;\n")
        if self.hasRequiredParam():
            content.append("import com.renren.mobile.rmsdk.core.annotations.RequiredParam;\n")
        if self.hasOptionalParam():
            content.append("import com.renren.mobile.rmsdk.core.annotations.OptionalParam;\n")
        if self.needSessionKey == -1:
            content.append("import com.renren.mobile.rmsdk.core.annotations.NoSessionKey;\n")
        elif self.needSessionKey == 0:
            content.append("import com.renren.mobile.rmsdk.core.annotations.OptionalSessionKey;\n")
        content.append("\n")
        # class annotations
        content.append('@RestMethodName("%s")\n' % self.restMethodName)
        if self.needSessionKey == -1:
            content.append("@NoSessionKey\n")
        elif self.needSessionKey == 0:
            content.append("@OptionalSessionKey\n")
        # class name
        content.append("public class %sRequest extends RequestBase<%sResponse> {\n" % (classNamePrefix, classNamePrefix))
        # properties declaration
        indentation = 1
        for field in self.fields:
            content.append(field.getFieldRequiredOrOptional(indentation))
            content.append(field.getFieldDeclaration(indentation))

        # constructor method
        content.append("\tprotected %sRequest() {\n" % classNamePrefix)
        content.append("\t\tsuper();\n")
        content.append("\t}\n")
        content.append("\n")

        # setter and getter methods declaration
        for field in self.fields:
            # get method
            content.append(field.getGetterMethod(indentation))
            # set method
            content.append(field.getSetterMethod(indentation))

        # inner builder class
        content.append("\tpublic static class Builder {\n")
        content.append("\t\tprivate %sRequest request;\n" % classNamePrefix)
        content.append("\n")
        content.append("\t\tpublic Builder(")
        requiredParams = self.getRequiredParams()
        for index, field in enumerate(requiredParams):
            content.append("%s %s" % (field.getRealType() ,field.getRealName()))
            if index != len(requiredParams) - 1:
                content.append(", ")
        content.append(") {\n")
        content.append("\t\t\trequest = new %sRequest();\n" % classNamePrefix)
        for field in requiredParams:
            realName = field.getRealName()
            methodName = realName[0].capitalize() + realName[1:]
            content.append("\t\t\trequest.set%s(%s);\n" % (methodName, realName))
        content.append("\t\t}\n")
        content.append("\n")
        for field in self.getOptionalParams():
            realName = field.getRealName()
            methodName = realName[0].capitalize() + realName[1:]
            content.append("\t\tpublic Builder set%s(%s %s) {\n" % (methodName, field.getRealType(), realName))
            content.append("\t\t\trequest.set%s(%s);\n" % (methodName, realName))
            content.append("\t\t\treturn this;\n")
            content.append("\t\t}\n")
            content.append("\n")
        content.append("\t\tpublic %sRequest create() {\n" % classNamePrefix)
        content.append("\t\t\treturn request;\n")
        content.append("\t\t}\n")
        content.append("\t}\n")
        content.append("\n")

        # end of request class
        content.append("}\n")

        f.write(''.join(content))
        f.close()


responses = dict()
isValid = False
response = None
field = None
with open(RESPONSE_FILE) as f:
    for line in f:
        if not isValid:
            match = re.search(r'\s*message\s+(\w+)\s*{\s*', line)
            if match:
                isValid = True;
                response = Response()
                responses[match.group(1)] = response
        else:
            match = re.search(r'\s*(\w+)\s+(\w+)\s+(\w+)\s*=\s*(\d)\s*', line)
            if match:
                field = Field()
                field.property = match.group(1)
                field.type = match.group(2)
                field.name = match.group(3)
                order = match.group(4)
                field.order = order

                response.fields.append(field)
            elif re.search(r'\s*}\s*' ,line):
                # End of of a message body.
                isValid = False
                response = None
                field = None
            else:
                pass


requests = dict()
request = None
with open(REQUEST_FILE) as f:
    for line in f:
        if not isValid:
            match = re.search(r'\s*message\s+(\w+)\s*{\s*', line)
            if match:
                isValid = True;
                request = Request()
                requests[match.group(1)] = request
        else:
            match = re.search(r'\s*(\w+)\s+(\w+)\s+(\w+)\s*(=\s*(\d)\s*)?', line)
            if match:
                field = Field()
                field.property = match.group(1)
                field.type = match.group(2)
                field.name = match.group(3)
                if match.group(4):
                    field.default = match.group(5)
                request.insertField(field)
            elif re.search(r'\s*}\s*' ,line):
                # End of of a message body.
                isValid = False
                request = None
                field = None
            else:
                pass


apis = dict()
with open(APIS_FILE) as f:
    for line in f:
        if not line.startswith('#') and not line.isspace():
            name, value = line.split('=')
            apis[name] = value.rstrip()

for key in apis.keys():
    requestName, responseName = apis[key].split(',')
    request = requests[requestName]
    response = responses[responseName]

    request.restMethodName = key
    request.generateJavaSource()

    response.restMethodName = key
    response.generateJavaSource(responses)
                                                                                                                                                                                                                                                           AutoGenerationApis/requests.proto                                                                   000644  001751  001751  00000041627 11727616542 021020  0                                                                                                    ustar 00tristan                         tristan                         000000  000000                                                                                                                                                                         message ClientLoginRequest {
	required string user
	required string password
	required string uniq_id
	optional int32	isverify
	optional string verifycode
	optional string client_info
}

message ClientGetLoginInfoRequest {
	required string session_key
	optional string client_info
}

message FeedGetRequest {
	required string session_key
	required string type
	optional int32	page = 1
	optional int32	page_size = 30
	optional int64	uid
	optional int32 	focus
	optional string client_info
}

message FeedReadRequest {
	required string session_key
	required int64	id
	optional int32	is_mini_feed
	optional string client_info
}

message FeedPublishFeedRequest {
	required string session_key
	required string title
	required string url
	required string content
	optional string image_src
	optional string message
	optional string client_info
}

message VideoGetRequest {
	required string session_key
	required string video_url
	required string platform
	optional string client_info
}

message	VideoGetUrlRequest {
	required string session_key
	optional string client_info
}

message VideoSaveRequest {
	required string session_key
	required string	item_code
	required string title
	required string description
	optional string client_info
}

message ShareGetCommentsRequest {
	required string session_key
	required int64 	id
	required int64	user_id
	optional int32 	page = 1
	optional int32	page_size = 10
	optional int32	exclude_list
	optional int32	sort
	optional string client_info
}

message ShareAddCommentRequest {
	required string session_key
	required int64	id
	required int64	user_id
	required string content
	optional int64	rid
	optional string client_info
}

message ShareGetHotsRequest {
	required string session_key
	required int32	type
	optional int32	page = 1
	optional int32	page_size = 10
	optional int32	exclude_list
	optional string client_info
}

message	ShareGetsRequest {
	required string session_key
	optional int32	type
	optional int64	uid
	optional string sub_types
	optional int32	page = 1
	optional int32	page_size = 10
	optional int32	exclude_list
	optional string client_info
}

message ShareGetRequest {
	required string session_key
	required int64	id
	required int64	uid
	optional int32	type
	optional int32	with_source
	optional string password
	optional int32	only_desc
	optional int32	content_in_page
	optional int32	content_other_all
	optional int32	content_page = 1
	optional int32	content_page_size = 900
	optional string client_info
}

message SharePublishRequest {
	required string session_key
	required int64	id
	required int64	uid
	required int32	source_type
	optional int32	type
	optional string url
	optional string comment
	optional string password
	optional string client_info
}

message ShareDeleteRequest {
	required string session_key
	required int64	id
	optional int32	type
	optional string client_info
}

message SharePublishLinkRequest {
	required string session_key
	required string url
	required string title
	optional string thumb_url
	optional string desc
	optional string comment
	optional int32	from
	optional int32	page_id
	optional string client_info
}

message ShareGetLinkRequest {
	required string session_key
	required string url
	optional int32	content_size = 20
	optional string client_info
}

message GetsBlogRequest {
	required string session_key
	required int64	uid
	optional int32	page = 1
	optional int32	page_size = 10
	optional string client_info
}

message GetBlogRequest {
	required string session_key
	required int64	id
	required int64	user_id
	optional int32	need_html
	optional int32	only_br
	optional string	password
	optional int32	only_desc
	optional int32	content_in_page
	optional int32	content_other_all
	optional int32	content_page = 1
	optional int32	content_page_size = 900
	optional string client_info
}

message	AddBlogRequest {
	required string session_key
	required string title
	required string content
	optional int32	visible = 99
	optional string password
	optional string client_info
}

message	DeleteBlogRequest {
	required string session_key
	required int64	id
	optional string client_info
}

message	DeleteBlogCommentRequest {
	required string session_key
	required int64	id
	required int64	owner_id
	optional string client_info
}

message GetBlogCategoryRequest {
	required string session_key
	optional string client_info
}

message GetBlogCommentsRequest {
	required string session_key
	required int64	id
	required int64	user_id
	optional string password
	optional int32	page = 1
	optional int32	page_size = 10
	optional int32	sort
	optional string client_info
}

message	AddBlogCommentRequest {
	required string session_key
	required int64	id
	required string content
	required int64	user_id
	optional int64	rid
	optional int32	type
	optional string client_info
}

message BlogPrivacyRequest {
	required string session_key
	required int64	id
	required int64	owner_id
	optional string client_info
}

message GossipPostGossipRequest {
	required string session_key
	required int64	userId
	required string content
	optional int64	reUserId
	optional int32	isWhisper
	optional string client_info
}

message	GossipGetsRequest {
	required string session_key
	required int64	user_id
	optional int32	page = 1
	optional int32	page_size = 50
	optional string client_info
}

message GossipDeleteRequest {
	required string session_key
	required int64	id
	required int64	user_id
	optional string client_info
}

message FriendsGetFriendsRequest {
	required string session_key
	optional int64	userId
	optional int32	page = 1
	optional int32	pageSize = 30
	optional int32	hasNetwork
	optional int32	hasGroup
	optional int32	hasGender
	optional int32	hasIsFriend
	optional string client_info
}

message FriendsGetOnlineFriendsRequest {
	required string session_key
	optional int64	userId
	optional int32	isOnline
	optional int32	isContact
	optional int32	hasNetwork
	optional int32	hasGroup
	optional int32	hasGender
	optional int32	hasIsFriend
	optional int32	hasStatus
	optional int32	hasUserName
	optional int32	hasHeadUrl
	optional int32	useShortUrl
	optional int32	hasBirthday
	optional int32	hasLargeHeadUrl
	optional string client_info
}

message FriendsIsOnlineRequest {
	required string session_key
	optional string id_list
	optional string client_info
}

message FriendsSearchRequest {
	required string session_key
	required string name
	optional int32	page = 1
	optional int32	page_size = 30
	optional int32	hasSharedFriendsCount
	optional int32	hasIsFriend
	optional int32	hasNetwork
	optional int32	hasGender
	optional string client_info
}

message FriendsGetSharedFriendsRequest {
	required string sessioin_key
	required int64	userId
	optional int32	page = 1
	optional int32	pageSize = 30
	optional int32	exclude_list
	optional int32	hasFriendsCount
	optional int32	hasHeadImg
	optional int32	hasGender
	optional int32	hasIsVip
	optional int32	hasOnline
	optional int32	hasWapOnline
	optional int32	hasIsGuide
	optional int32	hasNetwork
	optional int32	hasGroup
	optional string client_info
}

message FriendsAreFriendsRequest {
	required string session_key
	required string user_id_list_1
	required string user_id_list_2
	optional string client_info
}

message FriendsRequestRequest {
	required string session_key
	required int64	uid
	optional string content
	optional string client_info
}

message FriendsAcceptRequest {
	required string session_key
	required int64	user_id
	optional string client_info
}

message	FriendsGetRequestsRequest {
	required string session_key
	optional int32	exclude_list
	optional int32	page = 1
	optional int32	page_size = 10
	optional int32	del_news
	optional string client_info
}

message FriendsDenyAllRequest {
	required string session_key
	optional string client_info
}

message FriendsDenyRequest {
	required string session_key
	required int64	user_id
	optional string client_info
}

message FriendsRecommendRequest {
	required string session_key
	optional int32	page = 1
	optional int32	page_size = 10
	optional string client_info
}

message FriendsRemoveFriendRequest {
	required string session_key
	required int64	uid
	optional string client_info
}

message FriendsAddFocusFriendRequest {
	required string session_key
	required int64	uid
	optional string client_info
}

message FriendsDelFocusFriendRequest {
	required string session_key
	required int64	uid
	optional string client_info
}

message FriendsGetFocusFriendsRequest {
	required string session_key
	optional string client_info
}

message NewsGetCountRequest {
	required string session_key
	optional int32	update_timestamp
	optional int32	total
	optional string sub_types
	optional int32	type
	optional string client_info
}

message	NewsGetClientCountRequest {
	required int64  last_time
	required int64	last_page_time
	optional string session_key
	optional string client_info
}

message NewsPushRequest {
	required string session_key
	required string sub_types
	required int32	type
	optional string client_info
}

message NewsNewsListRequest {
	required string session_key
	required string sub_types
	required int32	type
	optional int32	page = 1
	optional int32	page_size = 20
	optional bool	reflash
	optional string client_info
}

message NewsFriendRequestListRequest {
	required string session_key
	optional int32	page = 1
	optional int32	count = 30
	optional string client_info
}

message NewsReadNewsByIdRequest {
	required string session_key
	required int64	news_id
	optional string client_info
}

message NewsReadNewsBySourceIdRequest {
	required string session_key
	required int64 source_id
	required int32 type
	optional string client_info
}

message NewsGetFriendsBirthdayListRequest {
	required string session_key
	optional string client_info
}

message PhotosSendFeedRequest {
	required string session_key
	required int32	send_feed
	required int64	aid
	optional int32	from
	optional string client_info
}

message PhotosGetAlbumsRequest {
	required string session_key
	required int64	uid
	optional int64	aid
	optional int32	page = 1
	optional int32	page_size = 30
	optional string password
	optional int32	exclude_list
	optional int32	all_album
	optional int32	without_head
	optional string client_info
}

message PhotosGetRequest {
	required string session_key
	required int64	uid
	optional int64	aid
	optional int64	pid
	optional int32	page = 1
	optional int32	page_size = 10
	optional string password
	optional int32	all
	optional int32	exclude_list
	optional int32	with_lbs
	optional string client_info
}

message PhotosGetCoverRequest {
	required string session_key
	required int64	uid
	optional int64	pid
	optional string client_info
}

message PhotosGetNewUploadedRequest {
	required string session_key
	optional int64	uid
	optional int32	page = 1
	optional int32	page_size = 10
	optional int32	with_lbs
}

message PhotosGetCommentsRequest {
	required string session_key
	required int64	uid
	optional int64	aid
	optional int64	pid
	optional int32	page = 1
	optional int32	page_size = 10
	optional int32 	sort
	optional string password
	optional string client_info
}

message PhotosAddCommentRequest {
	required string session_key
	required int64	uid
	optional int64	aid
	optional int64	pid
	required string content
	optional int64	rid
	optional int32	whisper
	optional string client_info
}

message PhotosDeleteCommentRequest {
	required string session_key
	required int64	id
	required int64	uid
	optional int64	aid
	optional int64	pid
	optional string client_info
}

message PhotosCreateAlbumRequest {
	required string session_key
	required string name
	optional string description
	optional string location
	optional string password
	optional int32	visible
	optional string client_info
}

message PhotosDeleteRequest {
	required string session_key
	optional int64	pid
	optional int64	aid
	optional string client_info
}

message	PhotosEditRequest {
	required string session_key
	required int64	owner_id
	required int64	photo_id
	required int64	from_album_id
	optional int64	to_album_id
	optional string description
	optional int32	as_cover
	optional string client_info
}

message PhotosPrivacyRequest {
	required string session_key
	required int64	id
	required int64	owner_id
	optional int32	is_album
	optional string client_info
}

message PhotosAddTagRequest {
	required string session_key
	required int64	owner_id
	required int64	album_id
	required int64	photo_id
	required string tag_list
	optional string client_info
}

message PhotosGetTagsRequest {
	required string session_key
	required int64	owner_id
	required int64	photo_id
	optional string client_info
}

message PhotosDeleteTagRequest {
	required string session_key
	required int64	tag_id
	required int64	owner_id
	optional string client_info
}

message PhotosDeleteTagAllRequest {
	required string session_key
	required int64	photo_id
	required int64	owner_id
	optional string client_info
}

message StatusSetRequest {
	required string session_key
	required string status
	optional string place_data
	optional string client_info
}

message StatusForwardRequest {
	required string session_key
	required string status
	required int64	forward_doing_id
	required int64	forward_owner_id
	optional string place_data
	optional bool	send_owner
	optional bool	send_origin
	optional string client_info
}

message StatusGetRequest {
	required string session_key
	optional int64	uid
	optional int64	id
	optional string client_info
}

message StatusGetsRequest {
	required string session_key
	optional int64	uid
	optional int32	page = 1
	optional int32	page_size = 30
	optional string client_info
}

message StatusGetLastRequest {
	required string session_key
	required string user_id
	optional string client_info
}

message StatusAddCommentRequest {
	required string session_key
	required int64	owner_id
	required string content
	required int64	status_id
	optional int64	rid
	optional string client_info
}

message	StatusGetCommentsRequest {
	required string session_key
	required int64	id
	required int64	owner_id
	optional int32	page = 1
	optional int32	page_size = 20
	optional int32	with_status
	optional int32	sort
	optional string client_info
}

message StatusRemoveRequest {
	required string session_key
	required int64	status_id
	optional int64	owner_id
	optional string client_info
}

message StatusRemoveCommentRequest {
	required string session_key
	required int64	status_id
	required int64	comment_id
	optional int64	owner_id
	optional string client_info
}

message	StatusGetEmoticonsRequest {
	required string session_key
	optional string type
	optional int32	isall
	optional string client_info
}

message PageIsPageRequest {
	required string session_key
	required int64	page_id
	optional string client_info
}

message PageIsFansRequest {
	required string session_key
	required int64	user_id
	required int64	page_id
	optional string client_info
}

message	PageBecomeFanRequest {
	required string session_key
	required int64	page_id
	optional string ref
	optional string client_info
}

message PageQuitFansRequest {
	required string session_key
	required int64	page_id
	optional string client_info
}

message PageGetListRequest {
	required string session_key
	optional int32	page = 1
	optional int32	page_size = 10
	optional int64	user_id
	optional string client_info
}

message PageGetFansListRequest {
	required string session_key
	required int64	page_id
	optional int32	page = 1
	optional int32	page_size = 10
	optional string client_info
}

message PageGetInfoRequest {
	required string session_key
	required string fields
	required int64	page_id
	optional string client_info
}

message PageSearchRequest {
	required string session_key
	required string keyword
	optional int32	page = 1
	optional int32	page_size = 10
	optional string client_info
}

message PhoneclientGetUpdateInfoRequest {
	required string session_key
	required int	name
	required int	property
	required int	subproperty
	required string version
	required int	channelId
	required string ua
	required string os
	required int	pubdate
	required int	up
	optional string lastTag
	optional string client_info
}

message	PhoneclientActiveClientRequest {
	required string data
	required string uniq_id
	required string	client_info
}

message	PhoneclientActionLogRequest {
	required string data
	required string fromId
	required string terminal
	required string version
}

message PhoneclientSdkLogRequest {
	required string data
	required string app
	required string uid
	required string result
	required string fn
	required string	pf
	required string	ver
	optional string client_info
}

message PhoneclientGetErrorMsgRequest {
	required string session_key
	optional string	client_info
}

message PhoneclientToolLogRequest {
	required string time
	required string buttonId
	required string clickCount
	required string imei
	required string	contactCount
	optional string client_info
	optional string extraData
	optional string session_key
}

message PhoneclientGetRegexMsgRequest {
	required string regex_code
	optional string client_info
}

message PushAddTokenRequest {
	required string session_key
	required int	pusher
	required string token
	optional string	client_info
}

message PushAddWin8TokenRequest {
	required string session_key
	required int64	expired_time
	required string token
	optional string client_info
	optional int	sub_user_id
}

message BatchRunRequest {
	required string method_feed
	optional string client_info
	optional string session_key
}

                                                                                                         AutoGenerationApis/responses.proto                                                                  000644  001751  001751  00000113551 11725275117 021157  0                                                                                                    ustar 00tristan                         tristan                         000000  000000                                                                                                                                                                         package com.xiaonei.wap.mcs.proto.message;

option java_package = "com.xiaonei.wap.mcs.proto.message";
option java_outer_classname = "ApiMessage";

message ErrorResponse {
	required int32 error_code = 1;
	required string error_msg = 2;
}

message LoginResponse {
	required string session_key = 1;
	required string ticket = 2;
	required int32 uid = 3;
	required string secret_key = 4;
	required string user_name = 5;
	required string head_url = 6;
	required int64 now = 7;
	optional int32 login_count = 8;
	optional int32 fill_stage = 9;
}

message RegisterResponse {
	required int32 status = 1;
	required string msg = 2;
}

message SubmitResponse {
	required int32 result = 1;
}

//friends api response messages
message FriendsSearchResponse {
	required int32 total = 1;
	repeated FriendResponse friends = 2;
}

message FriendResponse {
	required int32 user_id = 1;
	optional string user_name = 2;
	optional string head_url = 3;
	optional int32 is_online = 4;
	optional int32 shared_friends_count = 5;
	optional int32 is_friend = 6;
	optional string network = 7;
	optional string group = 8;
	optional string gender = 9;
	optional string status = 10;
	optional int32 is_contact = 11;
	optional ProfileInfoBirthResponse birthday = 12;
}

message MyFriendsListResponse {
	required int32 count = 1;
	repeated FriendResponse friend_list = 2;
	optional string prefix_url = 3;
}

message FriendInfoResponse{
    required int32 user_id_1 = 1;
    required int32 user_id_2 = 2;
    required int32 are_friends = 3;
}

message FriendInfoListResponse{
    required int32 count = 1;
    repeated FriendInfoResponse friend_info_list = 2;
}

message FriendApplyResponse{
    required int32 user_id = 1;
    required string user_name = 2;
    required string head_url = 3;
    required string content = 4;
    required int32 share_count = 5;
}

message FriendApplyListResponse{
    required int32 count = 1;
    required int32 page_size = 2;
    repeated FriendApplyResponse friend_apply_list = 3;
}

//@ response messages
message AtSuggestResponse {
	required int32 total = 1;
	repeated FriendListModelResponse at_list = 2;
}

message FriendListModelResponse {
	required int32 user_id = 1;
	required string user_name = 2;
	required string head_url = 3;
	optional string network = 4;
}

//phone client response messages
message UpdateConfigResponse{
	required string leftKey = 1;
	required string rightKey = 2;
	required string title = 3;
}
message UpdateInfoResponse {
	required UpdateConfigResponse configInfo = 1;
	required string info = 2;
	required int32 pubdate = 3;
	required int32 type = 4;
	required string url = 5;
	optional string lastTag = 6;
	optional string version = 7;
	optional string introUrl = 8;
}


message UploadContactResponse {
	optional int32 search = 1;
	optional int32 add = 2;
	optional int32 modify = 3;
	optional int32 delete = 4;
	optional string get = 5;
}

message UploadContactGetResponse {
	required int64 id = 1;
	required string uptime = 2;
	required int32 deleted = 3;
	required string name = 4;
	required string nick = 5;
	optional string pn = 6;
	optional string pn2 = 7;
	optional int64 pn_uid = 8;
	optional int64 pn2_uid = 9;
	optional int32 pn_s = 10;
	optional int32 pn2_s = 11;
	required string tel = 12;
	required string fax = 13;
	required string eml = 14;
	required string eml2 = 15;
	required string company = 16;
	required string dpart = 17;
	required string job = 18;
	required string bday = 19;
	required int64 rruid = 20;
	required string url = 21;
	required string note = 22;
	required bytes photo = 23;
}

message UploadContactGetListResponse {
	repeated UploadContactGetResponse get_list = 1;
}

message MobileDataResponse{
	repeated string k = 1;
}

//batch run response messages
message BatchRunResponse {
	required int32 batch_num = 1;
}

message LbsDataResponse {
	optional int64 id = 1;
	optional string pid = 2;
	optional string pname = 3;	
	optional int64 latitude = 4;	
	optional int64 longitude = 5;
	optional string location = 6;
	optional string comment = 7;
}

message DoingResponse {
	required int64 id = 1;
	required int32 user_id = 2;
	required int64 time = 3;
	required string content = 4;
	required int32 comment_count = 5;
	required string user_name = 6;
	required string head_url = 7;
	optional DoingResponse origin = 8;
	optional LbsDataResponse lbs_data = 9;
	optional int32 forward_count = 10;
}

message EmoticonResponse {
	required string emotion = 1; 
	required string icon = 2; 
	required string desc = 3;
	optional int32 id = 4;
}

message EmoticonGroupResponse {
	required int32 id = 1;
	required string name = 2;
	repeated EmoticonResponse emoticon_list = 4; 
}

message EmoticonListResponse {
	required string base_url = 1;
	repeated EmoticonResponse emoticon_list = 2;
	repeated EmoticonGroupResponse emoticon_group_list = 3;
	optional int64 version = 4;
}

message DoingListResponse{
	required int32 count = 1;
	repeated DoingResponse status_list = 2;
}

message LastDoingResponse {
	required int32 user_id = 1;
	required int64 id = 2;
	required string content = 3;
	required int64 do_time = 4;
	required int32 comment_count = 5;
}

message LastDoingListResponse{
	required int32 count = 1;
	repeated LastDoingResponse status_list = 2;
}

message DoingCommentResponse {
	required int64 id = 1;
	required int32 user_id = 2;
	required string user_name = 3;
	required string content = 4;
	required int64 time = 5;
	required string head_url = 6;
}

message DoingCommentListResponse {
	required int32 count = 1;
	repeated DoingCommentResponse comment_list = 2;
	required int32 page_size = 3;
	optional DoingResponse status = 4;
}

message RadioResponse{
	required int64 id = 1;
	required string name = 2;
	required string bg = 3;
}

message RadioUserResponse{
	required int64 id = 1;
	required string name = 2;
	required string tinyUrl = 3;
}

message RadioSongResponse{
	required int64 id = 1;
	required string name = 2;
	required int64 artistId = 3;
	required string artistName = 4;
	required string src = 5;
	required int64 duration = 6;
	required string lyric  = 7;
	required string albumImg = 8;
	required string albumInfo = 9;
	required bool fav = 10;
	required string albumName = 11;
}

message RadioGetHomeResponse{
	repeated RadioResponse radios = 1;
	repeated RadioSongResponse songs = 2;
	required string uuid = 3;
	required int32 currentRadio = 4;
}

message RadioGetHomeLogonResponse{
	repeated RadioResponse radios = 1;
	repeated RadioSongResponse songs = 2;
	required RadioUserResponse user = 3;
	required string uuid = 4;
	required int32 currentRadio = 5;
}

message RadioGetRadioResponse{
	repeated RadioSongResponse songs = 1;
}

message RadioGetSongByNamesResponse{
	required int64 id = 1;
	required string albumSmallImg = 2;
	required string albumMiddleImg = 3;
	required string albumBigImg = 4;
	required string songName = 5;
	required string artistName = 6;
	required string albumName = 7;
}

message FeedAttachmentResponse{
	required string url = 1;
	required string type = 2;
	optional string src = 3;
	optional int64 media_id = 4;
	optional int32 owner_id = 5;
	optional string digest = 6;
	optional string main_url = 7;
}

message FeedCommentResponse{
	required int64 id = 1;
	required int32 user_id = 2;
	required string user_name = 3;
	required string head_url = 4;
	optional int64 time = 5;
	optional string str_time = 6;
	required string content = 7;
}

message FeedLikeResponse{
	optional int32 total_count = 1;
	optional int32 friend_count = 2;
	optional int32 i_like = 3;
	repeated int32 user_list = 4;
}

message FeedShareResponse{
	optional int64 source_id = 1;
	optional int32 owner_id = 2;
	optional string owner_name = 3;
	optional string comment = 4;
	optional string url = 5;
	optional string video_url = 6;
	optional int32 video_support = 7;
	optional string forward_comment = 8;
	optional string forward_meta = 9;
}

message FeedStatusForwardResponse{
	optional int64 id = 1;
	optional string status = 2;
	optional int32 owner_id = 3;
	optional string owner_name = 4;
}

message FeedResponse{
	required int64 id = 1;
	required int64 source_id = 2;
	required int32 type = 3;
	optional int64 time = 4;
	optional string str_time = 5;
	required int32 user_id = 6;
	required string user_name = 7;
	required string head_url = 8;
	optional string prefix = 9;
	optional string content = 10;
	optional string title = 11;
	optional string url = 12;
	optional string description = 13;
	repeated FeedAttachmentResponse attachement_list = 14;
	optional int32 comment_count = 15;
	repeated FeedCommentResponse comment_list = 16;
	optional FeedLikeResponse likes = 17;
	optional int32 origin_type = 18;
	optional string origin_title = 19;
	optional string origin_img = 20;
	optional int32 origin_page_id = 21;
	optional string origin_url = 22;
	optional LbsDataResponse place = 23;
	optional FeedShareResponse share = 24;
	optional FeedStatusForwardResponse status_forward = 25;
	optional int32 photo_count = 26;
	optional int32 page_checked = 27;
	optional string page_image_url = 28;
	optional string head_link = 29;
	optional int32 link_type = 30;
}

message FeedGetResponse{
	repeated FeedResponse feed_list = 1;
	optional int32 has_more = 2;
	optional int32 is_mini_feed = 3;
}

message VFeedGetResponse{
	optional string feed_list = 1;
	optional int32 code = 2;
}

message UserResponse{
	required int32 user_id = 1;
	optional string user_name = 2;
	optional string head_url = 3;
	optional string gender = 4;
	optional int32 is_vip = 5;
	optional int32 is_online = 6;
	optional int32 is_wap_online = 7;
	optional int32 is_guide = 8;
	optional int32 friends_count = 9;
	optional string network = 10;
	optional string group = 11;
}
message FriendsSharedResponse{
	required int32 count = 1;
	repeated UserResponse friend_list = 2;
}

message VideoGetResponse{
	required string name = 1;
	required int64 time = 2;
	required int32 play_number = 3;
	required float rating = 4;
	required string src_fluency = 5;
	required int32 type_fluency = 6;
	required string src_clear = 7;
	required int32 type_clear = 8;
	required string introduction = 9;
	repeated string pictures = 10;
}

message ShareCommentResponse {
	required int64 id = 1;
	required int32 user_id = 2;
	required string user_name = 3;
	required string head_url = 4;
	required int64 time = 5;
	required string content = 6;
}

message ShareCommentListResponse {
	required int32 count = 1;
	repeated ShareCommentResponse comment_list = 2;
}

message ShareItemResponse {
	required int64 id = 1;
	required int32 type = 2;
	required int64 time = 3;
	optional string str_time = 4;
	optional int64 source_id = 5;
	optional int32 source_owner_id = 6;
	optional string source_owner_name = 7;
	optional string title = 8;
	optional string photo = 9;
	optional string url = 10;
	optional string description = 11;
	optional int32 user_id = 12;
	optional string user_name = 13;
	optional string head_url = 14;
	optional string video_url = 15;
	optional int32 video_support = 16;
	optional BlogResponse blog_info = 17;
	optional AlbumInfoResponse album_info = 18;
	optional PhotoInfoResponse photo_info = 19;
	optional int32 comment_count = 20;
	optional int32 share_count = 21;
	optional int32 view_count = 22;
	optional int64 share_id = 23;
	optional string forward_comment = 24;
}

message ShareGetsResponse {
	required int32 count = 1;
	repeated ShareItemResponse item_list = 2;
}

message NewsResponse{
	repeated int64 id = 1;
	required int32 type = 2;
	required int64 time = 3;
	repeated int32 user_id = 4;
	repeated string user_name = 5;
	repeated string head_url = 6;
	optional int64 source_id = 7;
	optional int32 owner_id = 8;
	optional string owner_name = 9;
	optional string prefix = 10;
	optional string title = 11;
	optional string sufix = 12;
	optional string brief = 13;
	optional int32 latest = 14;
	optional int32 user_count = 15;
}

message NewsListResponse{
	repeated NewsResponse news_list = 1;
	optional int32 count = 2;
	optional int32 page_size = 3;
}

message NewsTotalResponse {
	optional int32 gossip_reply_count = 1;
	optional int32 message_count = 2;
	optional int32 friend_request_count = 3;
	optional int32 news_count = 4;
	optional int32 app_invite_count = 5;
	optional int32 app_page_feed_count = 6;
	optional int32 home_feed_count = 7;
	optional int64 now = 8;
}

message FriendBirthDayResponse{
	required int32 user_id = 1;
	required string user_name = 2;
	required string head_url = 3;
	required string birthday = 4;
}

message FriendBirthDayListResponse{
	repeated FriendBirthDayResponse birthday_list = 1;
}

message AlbumCreateResponse{
	required int32 result = 1;
	optional int64 album_id = 2;
}

message PhotosUploadResponse{
	required int64 photo_id = 1;
	required int64 album_id = 2;
	required int32 user_id = 3;
	required string img_head = 4;
	required string img_main = 5;
	required string img_large = 6;
	required string caption = 7;
}
message PhotosCoverResponse{
	required int64 photo_id = 1;
	required int32 user_id = 2;
	required string img_origin = 3;
	optional string img_main = 4;
	optional string img_large = 5;
	optional string caption = 6;
}

message PhotoInfoResponse{
	required int64 id = 1;
	required int64 album_id = 2;
	required int32 user_id = 3;
	optional string img_head = 4;
	optional string img_large = 5;
	optional string caption = 6;
	optional int64 time = 7;
	optional string time_str = 8;
	optional int32 view_count = 9;
	optional int32 comment_count = 10;
	optional LbsDataResponse lbs_data = 11;
	optional string album_name = 12;
	optional string user_name = 13;
}

message PhotoListResponse{
	required int32 count = 1;
	repeated PhotoInfoResponse photo_list = 2;
	optional string album_name = 3;
}

message AlbumInfoResponse{
	required int64 id = 1;
	required string img = 2;
	required string title = 3;
	optional int64 create_time = 4;
	optional int64 upload_time = 5;
	optional string description = 6;
	optional string location = 7;
	optional int32 size = 8;
	optional int32 visible = 9;
	optional int32 comment_count = 10;
	optional int32 user_id = 11;
	optional string user_name = 12;
	optional string head_url = 13;
	optional int32 has_password = 14;
	optional int32 album_type = 15;
}

message AlbumListResponse{
	required int32 count = 1;
	repeated AlbumInfoResponse album_list = 2;
}

message PhotoCommentResponse{
	required int64 id = 1;
	required int32 user_id = 2;
	required string user_name = 3;
	required string head_url = 4;
	required string content = 5;
	required int64 time = 6;
	optional int64 source_id = 7;
	optional int32 owner_id = 8;
	optional int32 to_user_id = 9;
	optional int32 whisper = 10;
	optional int32 from_mobile = 11;
}

message PhotoCommentListResponse{
	required int32 count = 1;
	repeated PhotoCommentResponse comment_list = 2;
}

message BlogAddResultResponse {
	required int64 id = 1;
}

message PhotoTagListResponse {
	required int32 count = 1;
	repeated PhotoTagResponse tag_list = 2;
}

message PhotoTagResponse {
    required int32 id = 1;
    required int64 frame_height = 2;
	required int64 frame_width = 3;
	required int64 left_to_photo = 4;
	required int64 top_to_photo = 5;
	required int32 target_id = 6;
	required string target_name = 7;
}

message BlogCommentResponse {
	required int64 id = 1;
	required int32 user_id = 2;
	required string user_name = 3;
	required string head_url = 4;
	required int64 time = 5;
	required string content = 6;
	required int32 whisper = 7;
}

message BlogCommentListResponse {
	required int32 count = 1;
	repeated BlogCommentResponse comment_list = 2;
}

message BlogResponse {
	required int64 id = 1;
	required int32 user_id = 2;
	required string user_name = 3;
	required string head_url = 4;
	required string title = 5;
	required int64 time = 6;
	required string content = 7; 
	required int32 view_count = 8;
	required int32 comment_count = 9;
	required int32 visible = 10;
	optional int32 content_page_count = 11;
	optional int32 share_count = 12;
}

message BlogShortResponse {
	required int64 id = 1;
	required int64 time = 2;
	required string cate = 3;
	required string title = 4;
	required string content = 5;
	required int32 view_count = 6;
	required int32 comment_count = 7;
	required int32 visible = 8;
}

message BlogListResponse {
	required int32 user_id = 1;
	required string user_name = 2;
	required int32 count = 3;
	repeated BlogShortResponse blog_list = 4;
}

message BlogCategoryResponse{
    required int32 id = 1;
    required string category_name = 2;
}

message BlogCategoryListResponse{
    required int32 count = 1;
    repeated BlogCategoryResponse category_list = 2;
}

//message api response message
message MessageResponse{
    required int32 id = 1;
    required int32 user_id = 2;
    required string user_name = 3;
    required string head_url = 4;
    required int64 time = 5;
    required string title = 6;
    required string content = 7;
    required int32 is_read = 8;
    required int32 is_out_message = 9;
}

message MessageListResponse{
    required int32 unread_count = 1;
    required int32 count = 2;
    required int32 page_size = 3;
    repeated MessageResponse message_list = 4;
}

message MessageReplyItemResponse{
    required int32 user_id = 1;
    required string user_name = 2;
    required string head_url = 3;
    required int64 time = 4;
    required string content = 5;
}

message MessageReplyItemList{
    required int32 count = 1;
    required string title = 2;
    required int32 is_out_message = 3;
    repeated MessageReplyItemResponse reply_list = 4;
}

message UserVisitorResponse{
	required int32 user_id = 1;
	required string user_name = 2;
	required string user_head = 3;
	required int64 time = 4;
	required int32 is_online = 5;
	required int32 gender = 6;
	optional int32 is_friend = 7;
	optional int32 share_friends_count = 8;
}

message UserVisitorListResponse{
    required int32 count = 1;
    required int32 page_size = 2;
	repeated UserVisitorResponse visitor_list = 3;
}

//gossip api response message
message GossipResponse{
    required int64 id = 1;
    required int32 user_id = 2;
    required string user_name = 3;
    required string head_url = 4;
    required string content = 5;
    required int64 time = 6;
    required int32 whisper = 7;
    required int32 source = 8;
    required string large_url = 9;
}

message GossipListResponse{
    required int32 count = 1;
    required int32 page_size = 2;
    required int32 has_more = 3;
    repeated GossipResponse gossip_list = 4;
}

message ProfileInfoBirthResponse{
	optional string year = 1;
	optional int32 month = 2;
	optional int32 day = 3;
}

message ProfileInfoStatusResponse{
	required int64 id = 1;
	required string content = 2;
	required int64 time = 3;
	optional int32 comment_count = 4;
}

message ProfileInfoResponse{
	required int32 user_id = 1;
	required string user_name = 2;
	required string head_url = 3;
	required int32 is_star = 4;
	repeated string network = 5;
	optional int32 gender = 6;
	optional ProfileInfoBirthResponse birth = 7;
	optional string hometown_province = 8;
	optional string hometown_city = 9;
	optional ProfileInfoStatusResponse status = 10;
	optional int32 is_friend = 11;
	optional int32 visitor_count = 12;
	optional int32 blog_count = 13;
	optional int32 album_count = 14;
	optional int32 friend_count = 15;
	optional int32 gossip_count = 16;
	optional int32 share_friend_count = 17;
	optional int32 has_right = 18;
	optional int32 vip_stat = 19;
	optional int32 vip_level = 20;
	optional string tiny_url = 21;
	optional string main_url = 22;
	optional PhotosCoverResponse cover_photo=23;
}

//Place
message PlaceActivityResponse {
	required string period_msg = 1;
	required string message = 2;
	required string activity_icon = 3;
	required string url = 4;
	required int32 type = 5;
}

message PlaceActivityCountResponse {
	required int32 count = 1;
    optional int32 need2deflect = 2;
    optional int32 locate_type = 3; 
    optional int64 lat_gps = 4;
    optional int64 lon_gps = 5;
	optional int64 lat_deflect = 6;
	optional int64 lon_deflect = 7;
}

message PlaceActivityListResponse {	
	required int32 count = 1 ;
	repeated PlaceActivityResponse activity_list = 2;
	required int32 page_size = 5;
}

message PlaceActivityPoiResponse {
    required string pid = 1;
    required string name = 2;
    required string activity_caption = 3;
    required string address = 4;
    required string url = 5;
    required string activity_contents = 6;
}

message PlaceActivityPoiListResponse { 
    required int32 count = 1 ;
    repeated PlaceActivityPoiResponse poi_list = 2;
    required int32 page_size = 5;
    optional int32 need2deflect = 6;
    optional int32 locate_type = 7; 
    optional int64 lat_gps = 8;
    optional int64 lon_gps = 9;
}

message PlaceFriendResponse {
	required int64 add_time = 1;
	required int32 data_type = 2;
	required int32 distance = 3;
	required string head_url = 4;
	required int64 latitude_gps = 5;
	required int64 latitude_poi = 6;
	required int64 locate_type = 7;
	required int64 longitude_gps = 8;
	required int64 longitude_poi = 9;
	required string main_url = 10;
	required string user_name = 11;
	required string pid = 12;
	required string poi_address = 13;
	required string poi_name = 14;
	required string poi_phone = 15;
	required int32 privacy = 16;
	required string status_text = 17;
	required string tiny_url = 18;
	required int32 user_id = 19;
	optional int64 lbs_id = 20;
	optional int64 source_id = 21;
}

message PlaceFriendListResponse {
	required int32 count = 1;
	repeated PlaceFriendResponse friends_list = 2;
	optional int64 lat_gps = 3;
	optional int64 lon_gps = 4;
	required int32 page_size = 5;
	optional int32 need2deflect = 6;
	optional int32 locate_type = 7;
	optional int64 lat_deflect = 8;
	optional int64 lon_deflect = 9; 
}

message PlacePoiResponse {
	optional int32 distance = 1;
	optional int64 lon = 2;
	optional string phone = 3;
	optional float weight = 4;
	optional string address = 5;
	optional string poi_name = 6;
	optional string pid = 7;
	optional int64 lat = 8;
	optional string activity_caption = 9;
	optional int32 activity_count = 10;
	optional int32 nearby_activity_count = 11;
	optional string county = 12;
	optional string street_name = 13;
	optional string nation = 14;
	optional string city = 15;
	optional string province = 16;
}

message PlacePoiListResponse {
	required int32 count = 1;
	required PlacePoiResponse info = 2;
	repeated PlacePoiResponse poi_list = 3;
	required int32 page_size = 4;
	optional int64 lat_gps = 5;
	optional int64 lon_gps = 6;
	optional int32 need2deflect = 7;
	optional int32 locate_type = 8;
}

message PlacePoiBaseInfoResponse {
	optional string pid = 1;
	required string poi_name = 2;
	required string poi_address = 3;
	required string map_url = 4;
	required int32 visit_count = 5;
	required int32 activity_count = 6;
	optional string activity_contents = 7;
	required int32 nearby_activity_count = 8;
	optional int64 lat = 9;
	optional int64 lon = 10;
	optional string activity_url = 11;
	optional string detail_address = 12;
}

message PlaceAddEvaluationResponse {
	required int32 result = 1;
	required string message = 2;
	required int64 lat_gps = 3;
	required int64 lon_gps = 4;
	required int32 need2deflect = 5;
	required int32 locate_type = 6;
}

message PlaceAddPoiResponse {
	required PlacePoiBaseInfoResponse base_info = 1;
	required int32 distance = 2;
	required int64 lat_gps = 3;
	required int64 lon_gps = 4;
	required int32 need2deflect = 5;
	required int32 locate_type = 6;
}

message PlaceCheckinResponse {
	required int64 lat_gps = 1;
	required int64 lon_gps = 2;
	required int32 need2deflect = 3;
	required int32 result = 4;
}

message PlaceCalculateDistanceResponse {
	required string pid = 1;
	required double distance = 2;
	required int64 lat_gps = 3;
	required int64 lon_gps = 4;
	required int32 need2deflect = 5;
	required int32 is_too_far_away = 6;
	required int32 locate_type = 7;
}

message PlaceFeedResponse {
	required int64 add_time = 1;
	required int32 data_type = 2;
	required int32 distance = 3;
	required string head_url = 4;
	required int64 latitude_gps = 5;
	required int64 latitude_poi = 6;
	required int64 locate_type = 7;
	required int64 longitude_gps = 8;
	required int64 longitude_poi = 9;
	required string main_url = 10;
	required string user_name = 11;
	required string pid = 12;
	required string poi_address = 13;
	required string poi_name = 14;
	required string poi_phone = 15;
	required int32 privacy = 16;
	required string status_text = 17;
	required string tiny_url = 18;
	required int32 user_id = 19;
	required int32 reply_count = 20;
	required string feed_image_url = 21;
	required int64 source_id = 22;
	optional FeedStatusForwardResponse status_forward = 23;
	optional int32 origin_type = 24;
    optional string origin_title = 25;
    optional string origin_url = 26;
    optional int64 media_id = 27;
    repeated FeedAttachmentResponse attachement_list = 28;
    optional int64 lbs_id = 29;
    optional string title = 30;
    optional string prefix = 31;
}

message PlaceFeedListResponse {
	required int32 count = 1;
	required int32 page_size = 2;
	repeated PlaceFeedResponse feed_list = 3;
	optional int32 locate_type = 4;
	optional int32 need2deflect = 5;
	optional int64 lat_gps = 6;
	optional int64 lon_gps = 7;
}

message PlaceLatLonResponse {
	required int64 lat = 1;
	required int64 lon = 2;
}

message PlaceDeflectLatLonResponse {
	required PlaceLatLonResponse latlon = 1;
	required int32 need2deflect = 2;
	required int32 locate_type = 3;
}

message PlaceEvaluationCommentResponse {
	required int64 id = 1;
	required string content = 2;
	required int32 user_id = 3;
	required string user_name = 4;
	required string head_url = 5;
	required int64 time = 6;
}

message PlaceEvaluationCommentListResponse {
	required int32 count = 1;
	repeated PlaceEvaluationCommentResponse comment_list = 2;
	required int32 page_size = 3;
	optional PlaceEvaluationResponse evaluation = 4;
}

message PlaceEvaluationResponse {
	required int64 id = 1;
	required int32 user_id = 2;
	required string content = 3;
	required int32 comment_count = 4;
	required int64 time = 5;
	optional LbsDataResponse place = 6;
}

message PlaceReplyListPCIResponse {
	required int64 id = 1;
	required string pid = 2;
	required int64 lat = 3;
	required int64 lon = 4;
	required int64 time = 5;
	required string p_address = 6;
	required int32 user_id = 7;
	required string user_name = 8;
	required string head_url = 9;
	optional string status = 10;
	required string poi_name = 11;
}

message PlaceReplyItem {
	required int64 id = 1;
	required int32 user_id = 2;
	required string user_name = 3;
	optional string head_url = 4;
	required string content = 5;
	required int64 time = 6;
}

message PlaceReplyListMessage {
	required int32 count = 1;
	optional PlaceReplyListPCIResponse pci = 2;
	repeated PlaceReplyItem reply_list = 3;
}

message PlacePoiCategoryResponse {
	required int64 id = 1;
	required string name = 2;
}

message PlacePoiCategoryListResponse {
	required int32 count = 1;
	repeated PlacePoiCategoryResponse category_list = 2;
}

//page message define
message PageResponse{
    required int32 id = 1;
    required string page_name = 2;
    required string head_url = 3;
    required string desc = 4;
    required string classification = 5;
    required int32 fans_count = 6;
    required int32 is_fan = 7;
    required int32 is_checked = 8;
}

message PageListResponse{
    required int32 count = 1;
    required int32 page_size = 2;
    repeated PageResponse page_list = 3;
}

message FansResponse{
    required int32 user_id = 1;
    required string user_name = 2;
    required string head_url = 3;
}

message FansListResponse{
    required int32 count = 1;
    required int32 page_size = 2;
    repeated FansResponse fans_list = 3;
}

message PageStatusResponse{
    required int64 status_id = 1;
    required string content = 2;
    required int64 time = 3;
}

message PageMapResponse{
    required string key = 1;
    required string value = 2;
}

message PageInfoResponse{
    required int32 id = 1;
    required string page_name = 2;
    required string head_url = 3;
    required int32 is_fan = 4;
    required int32 is_checked = 5;
    optional PageStatusResponse status = 6;
    optional string desc = 7;
    repeated PageMapResponse base_info = 8;
    repeated PageMapResponse detail_info = 9;
    repeated PageMapResponse contact_info = 10;
    optional int32 albums_count = 11;
    optional int32 blogs_count = 12;
    optional int32 fans_count = 13;
}


message ContactTalkContactListResponse {
	required int32 count = 1;
	repeated ContactTalkContactResponse contact_list = 2;
}

message ContactTalkContactResponse {
	optional int32 user_id = 1;
	optional string head_url = 2;
	optional string large_head_url = 9;
	optional int32 serial_number = 3;
	optional string name = 4;
	optional int32 friend = 5;
	optional int32 contact_friend = 6;
	optional int32 contact_type = 7;
	repeated ContactTalkPhoneNumberResponse phone_number_list = 8;
}

message ContactTalkPhoneNumberResponse {
	required string phone_number = 1;
	optional int32 from_web_contact = 2;
	optional int32 from_local_contact = 3;
	optional int32 from_bind = 4;
	required int32 cell_phone =5;
}

message ContactRecommendResponse {
    required int32 user_id = 1;
    required string user_name = 2;
    required string head_url = 3;
}

message ContactQuasiFriendResponse {
    required int32 serial_number = 1;
    optional string name = 2;
    optional string first_name = 3;
    optional string last_name = 4;
    required string phone_number = 5;
}

message ContactUpdateResponse{
    required int32 serial_number = 1;
    required string head_url = 2;
    optional string profile_url = 3;
    required int32 user_id = 4;
    optional ProfileInfoBirthResponse birthday = 5;
}

message ContactRenrenContactResponse {
    required string profile_url = 1;
    required string user_name = 2;
    required string head_url = 3;
    required string phone_number = 4;
    required int32 user_id = 5;
    optional ProfileInfoBirthResponse birthday = 6;
}

message ContactSynchronizeResponse {
    repeated ContactUpdateResponse update_list = 1;
    repeated ContactRecommendResponse recommend_list = 2;
    repeated ContactQuasiFriendResponse quasifriend_list = 3;
    repeated ContactRenrenContactResponse renren_contact_list = 4;
}

message ContactNeed2SynchronizeResponse {
    required int32 result = 1 ;
    required int64 date = 2;
}

message ContactDetailResponse {
	optional int32 serial_number = 1;
	required int32 user_id = 2;
	required string name = 3;
	required string head_url = 4;
	required string sex = 5;
	optional ProfileInfoBirthResponse birthday = 6;
	repeated string addr = 7;
	repeated string qq = 8;
	repeated string msn = 9;
	repeated ContactTalkPhoneNumberResponse phone_number_list = 10;
	repeated string email = 11;
	required string profile_url = 12;
	required int32 contact_type = 13;
	required int32 friend = 14;
	optional string astrology = 15;
}

message SocialMajordomoLastUploadDateResponse {
	required int32 result = 1;
	required int64 date = 2;
}

message SocialMajordomoLastCommInfoResponse {
	required string phone_number = 1;
	required string type = 2;
	required int64 date = 3; 

}

message SocialMajordomoLastCommResponse {
	repeated SocialMajordomoLastCommInfoResponse last_comminfo_list = 1;
}

message SocialMajordomoCommInfoResponse {
	required int32 week = 1;
	required string phone_number = 2;
	required int32 initiative_call = 3;
	required int32 total_initiative_call = 4;
	required int32 passive_call = 5;
	required int32 total_passive_call = 6;
	required int32 initiative_message = 7;
	required int32 total_initiative_message = 8;
	required int32 passive_message = 9;
	required int32 total_passive_message = 10;
	required int32 repeat_count = 11;
	required int32 out_duration = 12;
	required int32 in_duration = 13;
	required int32 day_call =14;
	required int32 night_call = 15;
	required int32 day_message =16;
	required int32 night_message = 17;
}

message SocialMajordomoDownloadResponse {
	repeated SocialMajordomoCommInfoResponse comminfo_list = 1;
}

message SocialMajordomoCardResponse {
	required string key = 1;
	required string value = 2;
	required int32 type = 3;
	required int32 subtype = 4;
}

message SocialMajordomoCardDownloadResponse {
	repeated SocialMajordomoCardResponse card_list = 1;
}

// talk
message TalkSendResultResponse {
	optional int32 code = 1;
	optional string msg = 2;
}

message TalkVoiceUploadResponse{
	required int32 result = 1;
	optional string msg = 2;
	required string vid = 3;
	optional string url = 4;
}

// blog and photo privacy
message PrivacyResponse{
	required int32 privacy_level = 1;
}

message UrlResponse {
	repeated string urls = 1;
}

message RegisterInfoResponse {
	required string register_info = 1;
	optional string long_number = 2;
}

message ShareGetLinkResponse {
	required string title = 1;
	repeated string imageUrl_list = 2;
	required string content = 3;
}

message PhoneClientGetErrorMsgResponse {
	required int32 app_id = 1;
	required int32 count = 2;
	repeated ErrorResponse error_list = 3;
}


message VideoUploadeUrl{
	required string item_code = 1;
	required string url = 2;
}

message PoiSearchResultResponse{
	required int32 total = 1;
	repeated PoiDataResponse poiDataList = 2;
}

message PoiDataResponse{
	required string address = 1;
	required string city = 2;
	optional string city_code = 3;
	required double distance = 4;
	required string district = 5;
	required double latitude = 6;
	required double longitude = 7;
	required string map_url = 8;
	required string name = 9;
	required string phone_no = 10;
	required string pid = 11;
	required string poi_type = 12;
	required string province = 13;
	required string country = 14;
	required string direction = 15;
}

message GeoDataResponse{
	required double longitude = 1;
	required double latitude = 2;
	required string positionName = 3;
}

message ReverseGeoDataResponse{
	required double longitude = 1;
	required double latitude = 2;
	required string StreetName = 3;
	required string address = 4;
	required string district = 5;
	required string city = 6;
	required string cityCode = 7;
	required string province = 8;
	required string country = 9;
	required string nearestPoiName = 10;
	required string nearestPoiType = 11;
	required string nearestPoiDirection = 12;
	required string nearestPoiDistance = 13;
	required string nearestRoadName = 14;
	required string nearestRoadDirection = 15;
	required string nearestRoadDistance = 16;
	required string area = 17;
	required string village = 18;
	required string town = 19;
}

message LocateResultResponse{
	required double latitude = 1;
	required double longitude = 2;
	required string address = 3;
	required double accuracy = 4;
	required string nation = 5;
	required string province = 6;
	required string city = 7;
	required string district = 8;
	required string poiName = 9;
	required string direction = 10;
	required string distance = 11;
}

message LbsGetStaticMapResponse{
	required string static_MapUrl = 1;
	required double latitude = 2;
	required double longitude = 3;
	
}

message PhoneClientGetRegexMsgResponse{
	required string regex_msg = 1;
}

message AppInfoResponse {
	required string app_id = 1;
	required string app_name = 2;
	required string app_icon_url_small = 3;  
    optional string app_icon_url_large = 4;
	required int32 auth_level = 5;
	required string auth_desc = 6;
	required int32 page_id = 7;
	optional int32 private_login = 8;
}

message PlaceSavePoiDataResponse {
	required string pid = 1;
	required string code = 2;
	required string msg = 3;
}

message ExploreHotTagResponse {
	required string tag = 1;
	required bool sub = 2;
}
message ExploreHotTagListResponse {
	repeated ExploreHotTagResponse hots = 1;
}

message ExploreTagsResponse {
	repeated string tags = 1;
}
message ExplorePhotoWallResponse {
	required string tag = 1;
	required string pic_url = 2;
	required string id = 3;
	required bool sub = 4;
	required string title = 5;
	required int32 type = 6;
	required bool multi = 7;
}

message ExplorePhotoWallListResponse {
	repeated ExplorePhotoWallResponse wall = 1;
}

message ExplorePhotoResponse {
	repeated string pic_url = 1;
	optional string desc = 2;
	optional int32 count = 3;
	required bool album = 4;
}

message ExploreVideoResponse {
	required string video_url = 1;
	required string thumb_url = 2;
	optional string summary = 3;
}

message ExploreBlogResponse {
	required string title = 1;
	required string summary = 2;
	optional string thumb_url = 3;
}

message ExploreShareResponse {
	required int32 owner_id = 1;
	required int64 share_id = 2;
}

message ExploreContentResponse{
	required int32 type = 1;
	required int32 from = 2;
	repeated string tags = 3;
	required int32 share_count = 4;
	optional ExplorePhotoResponse photo = 5;
	optional ExploreVideoResponse video = 6;
	optional ExploreBlogResponse blog = 7;
	optional ExploreShareResponse share = 8;
}

message ExploreContentListResponse {
	repeated ExploreContentResponse contents = 1;
}

message PaymentCreateResponse {
	required int32 result = 1;
	optional string request_token = 2;
    optional string order_id=3;
}

message SmsResponse {
	required int32 count = 1;
	repeated SmsGroupResponse sms_group = 2;
}

message SmsGroupResponse {
	required int32 id = 1;
	required string name = 2;
	required int32 count = 3;
	repeated SmsInfoResponse sms_info = 4;
}

message SmsInfoResponse {
	required int32 id = 1;
	required string content = 2;
}

message LocationFlowLiteResponse {
	required int64 id = 1;
    required int32 userId = 2;
    required string userName = 3;
    required int64 srcId = 4;
    required string content = 5;
    required int32 bizType = 6;
}


message PoiDataExtraResponse {
	required int64 id = 1;
    required string pid = 2;
    required double longitude = 3;
    required double latitude = 4;
    required double longitudeGps = 5;
    required double latitudeGps = 6;
    required string name = 7;
    required string address = 8;
    required string phone = 9;
    required string note = 10;
    required string country = 11;
    required string province = 12;
    required string city = 13;
    required string cityCode = 14;
    required string district = 15;
    required string street = 16;
    required int32 sourceType = 17;
    required string poiCaption = 18;
    required string poiType = 19;
    required int32 ugc = 20;
    required int32 friendsPointsCount = 21;
    required int32 friendsPhotoCount = 22;
    required int32 friendsVisited = 23;
    required int32 totalVistited = 24;
    required int32 hasActivity = 25;
    repeated LocationFlowLiteResponse latestFriendsPhotosList = 26;
    repeated LocationFlowLiteResponse latestFriendsPointsList = 27;
}

message PlaceGetNearByRecommendPoiExtraListResponse {
	required int32 count = 1;
	repeated PoiDataExtraResponse poiDataExtraList = 2;
}
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       