from fastapi import FastAPI
from app.routes import i2r, r2d, r2c, r2d_ui

app = FastAPI()

# Include the routes from each module
app.include_router(i2r.router, prefix="/i2r", tags=["I2R"])
app.include_router(r2d.router, prefix="/r2d", tags=["R2D"])
app.include_router(r2c.router, prefix="/r2c", tags=["R2C"])
app.include_router(r2d_ui.router, prefix="/r2d-ui", tags=["R2D/UI"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Requirements to Design/Code API!"}
