import string
from fastapi import FastAPI, Request, Response
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
import json
from generate import generate_iesmopeserta, generate_iesmosemi, generate_lombaexternal
from fastapi.middleware.cors import CORSMiddleware
data_iesmo = json.load(open('datapeserta/iesmo.json'))
data_broadcast = json.load(open('datapeserta/broadcast.json'))
data_iqrama = json.load(open('datapeserta/iqrama.json'))
data_mico = json.load(open('datapeserta/mico.json'))
data_msc = json.load(open('datapeserta/msc.json'))




app = FastAPI(docs_url="/anfujn", redoc_url=None)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse({'success': False}, status_code=403)
   

@app.get('/iesmo')
def IESMO(nomer_peserta: str, request: Request, nama_benar: str = 'benar', file:bool = False): 
   res = [sub for sub in data_iesmo if sub['NOPER'] == nomer_peserta.upper()]
   if file == False:
          if len(res) == 0:
            return {'success':False, 'alasan': 'nomor peserta salah'}
          else:
            if nama_benar == 'benar':
                return {'nama':res[0]['NAMA'].upper(), 'bidang':res[0]['JURUSAN'].upper(), 'role': res[0]['ROLE'], 'file': request.url._url+'&file=True'}
            else:
                return {'nama':nama_benar.upper(), 'bidang':res[0]['JURUSAN'].upper(), 'role': res[0]['ROLE'], 'file': request.url._url+'&file=True'}
   else:
          if len(res) == 0:
            return {'success':False, 'alasan': 'nomor peserta salah'}
          else:
            if nama_benar == 'benar':
                if res[0]['ROLE'] == 'peserta':
                    data = generate_iesmopeserta(res[0]['NAMA'].upper(), res[0]['JURUSAN'].upper())
                    return Response(content=data, media_type="application/pdf")
                elif res[0]['ROLE'] == 'semifinalis':
                    data = generate_iesmosemi(res[0]['NAMA'].upper(), res[0]['JURUSAN'].upper())
                    return Response(content=data, media_type="application/pdf")
            else:
                if res[0]['ROLE'] == 'peserta':
                    data = generate_iesmopeserta(nama_benar.upper(), res[0]['JURUSAN'].upper())
                    return Response(content=data, media_type="application/pdf")
                elif res[0]['ROLE'] == 'semifinalis':
                    data = generate_iesmosemi(nama_benar.upper(), res[0]['JURUSAN'].upper())
                    return Response(content=data, media_type="application/pdf")


   

@app.get('/broadcast')
def BROADCAST(nomer_peserta: str, request: Request, nama_benar: str = 'benar', file:bool = False):
   res = [sub for sub in data_broadcast if sub['NOPER'] == nomer_peserta.upper()]
   if file == False:
          if len(res) == 0:
            return {'success':False, 'alasan': 'nomor peserta salah'}
          else:
            if nama_benar == 'benar':
                return {'nama':res[0]['NAMA'].upper(), 'role': 'PESERTA', 'file': request.url._url+'&file=True'}
            else:
                return {'nama':nama_benar.upper(), 'role': 'PESERTA', 'file': request.url._url+'&file=True'}
   else:
          if len(res) == 0:
            return {'success':False, 'alasan': 'nomor peserta salah'}
          else:
            if nama_benar == 'benar':
                data  = generate_lombaexternal(res[0]['NAMA'].upper(), 'broadcasting')
                return Response(content=data, media_type="application/pdf")
            else:
                data  = generate_lombaexternal(nama_benar.upper(), 'broadcasting')
                return Response(content=data, media_type="application/pdf")

@app.get('/msc')
def MSC(nomer_peserta: str, request: Request, nama_benar: str = 'benar', file:bool = False):
   res = [sub for sub in data_msc if sub['NOPER'] == nomer_peserta.upper()]
   if file == False:
          if len(res) == 0:
            return {'success':False, 'alasan': 'nomor peserta salah'}
          else:
            if nama_benar == 'benar':
                return {'nama':res[0]['NAMA'].upper(), 'role': 'PESERTA', 'file': request.url._url+'&file=True'}
            else:
                return {'nama':nama_benar.upper(), 'role': 'PESERTA', 'file': request.url._url+'&file=True'}
   else:
          if len(res) == 0:
            return {'success':False, 'alasan': 'nomor peserta salah'}
          else:
            if nama_benar == 'benar':
                data  = generate_lombaexternal(res[0]['NAMA'].upper(), 'msc')
                return Response(content=data, media_type="application/pdf")
            else:
                data  = generate_lombaexternal(nama_benar.upper(), 'msc')
                return Response(content=data, media_type="application/pdf")

@app.get('/iqrama')
def IQRAMA(nomer_peserta: str, request: Request, nama_benar: str = 'benar', file:bool = False):
   res = [sub for sub in data_iqrama if sub['NOPER'] == nomer_peserta.upper()]
   if file == False:
          if len(res) == 0:
            return {'success':False, 'alasan': 'nomor peserta salah'}
          else:
            if nama_benar == 'benar':
                return {'nama':res[0]['NAMA'].upper(), 'role': 'PESERTA', 'file': request.url._url+'&file=True'}
            else:
                return {'nama':nama_benar.upper(), 'role': 'PESERTA', 'file': request.url._url+'&file=True'}
   else:
          if len(res) == 0:
            return {'success':False, 'alasan': 'nomor peserta salah'}
          else:
            if nama_benar == 'benar':
                data  = generate_lombaexternal(res[0]['NAMA'].upper(), 'iqrama')
                return Response(content=data, media_type="application/pdf")
            else:
                data  = generate_lombaexternal(nama_benar.upper(), 'iqrama')
                return Response(content=data, media_type="application/pdf")

@app.get('/mico')
def MICO(nomer_peserta: str, request: Request, nama_benar: str = 'benar', file:bool = False):
   res = [sub for sub in data_mico if sub['NOPER'] == nomer_peserta.upper()]
   if file == False:
          if len(res) == 0:
            return {'success':False, 'alasan': 'nomor peserta salah'}
          else:
            if nama_benar == 'benar':
                return {'nama':res[0]['NAMA'].upper(), 'role': 'PESERTA', 'file': request.url._url+'&file=True'}
            else:
                return {'nama':nama_benar.upper(), 'role': 'PESERTA', 'file': request.url._url+'&file=True'}
   else:
          if len(res) == 0:
            return {'success':False, 'alasan': 'nomor peserta salah'}
          else:
            if nama_benar == 'benar':
                data  = generate_lombaexternal(res[0]['NAMA'].upper(), 'mico')
                return Response(content=data, media_type="application/pdf")
            else:
                data  = generate_lombaexternal(nama_benar.upper(), 'mico')
                return Response(content=data, media_type="application/pdf")
