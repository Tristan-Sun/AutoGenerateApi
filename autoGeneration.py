#! /usr/local/bin/python

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
