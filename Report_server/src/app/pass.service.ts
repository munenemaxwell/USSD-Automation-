import { Injectable } from '@angular/core';
import { HttpClient ,HttpHeaders} from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class PassService {

  _url:string='http://localhost:8000/status/'

  constructor(private http:HttpClient) { }

  get_status():Observable<any>{
   
    return this.http.get(this._url);
  
  }
}



