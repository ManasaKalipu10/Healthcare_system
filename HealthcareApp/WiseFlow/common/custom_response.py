from rest_framework.response import Response


class CustomResponse(Response):

    def __init__(
        self,data=None,message="Success",success=True,status_code=200
    ):
        print(data,message,status_code,'123')
        response = {
            "success": success,
            "message": message,
            "data": data
        }
        print("response",response)

        super().__init__(
            data=response,
            status=status_code
        )
