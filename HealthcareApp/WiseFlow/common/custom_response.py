from rest_framework.response import Response


class CustomResponse(Response):

    def __init__(
        self,result=None,message="Success",success=True,status_code=200
    ):

        response = {
            "success": success,
            "message": message,
            "result": result
        }

        super().__init__(
            data=response,
            status=status_code
        )