import falcon

from benchmark_common import emulator


class Liveness:
    def on_get(self, req: falcon.Request, res: falcon.Response) -> None:
        res.media = {"message": "We are live"}


class DBCall:
    def on_get(self, req: falcon.Request, res: falcon.Response) -> None:
        obj = emulator.sync_database_request()
        return obj


class Calculation:
    def on_get(self, req: falcon.Request, res: falcon.Response) -> None:
        obj = emulator.do_some_calculation()
        return obj


class Complete:
    def on_get(self, req: falcon.Request, res: falcon.Response) -> None:
        obj = emulator.sync_complete_scenario()
        return obj


app = falcon.API()
app.add_route("/api/live", Liveness())
app.add_route("/api/db-call", DBCall())
app.add_route("/api/calculation", Calculation())
app.add_route("/api/complete", Complete())
