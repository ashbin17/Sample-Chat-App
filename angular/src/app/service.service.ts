import { Injectable } from '@angular/core';
import { HttpClient} from '@angular/common/http';
import { Observable} from 'rxjs';

// const logUrl = 'http://127.0.0.1:8000/api/login/';
// const regUrl = 'http://127.0.0.1:8000/api/register/';
const Url = 'http://127.0.0.1:8000/api/';

@Injectable({
  providedIn: 'root'
})
export class ServiceService {

  constructor(private http: HttpClient) { }

 /* login(data:any): Observable<any>{
    return this.http.post(logUrl, data);
  }

  register(data:any): Observable<any>{
    return this.http.post(regUrl, data);
  }
*/
  getUserDetails(): Observable<any>{            //login details
    return this.http.get(Url+'userdetails/');
  }

  getAllUser(): Observable<any>{                //all user login details
    return this.http.get(Url+'allusers/');
  }

  addUserDetails(data: any): Observable<any>{   //add user details
    return this.http.post(Url+'adduserdetails/', data);
  }

  getCurrentUser(): Observable<any>{            //get user details
    return this.http.get(Url+'getuserdetails/')
  }

  edituserdetails(data: any): Observable<any>{
    return this.http.put(Url+'edituserdetails/', data)
  }

  UploadPhoto(val:any){
    return this.http.post(Url+'savefile/',val);
  }

  search(val:any): Observable<any>{
    return this.http.get(Url+'search/'+val);
  }

  getForeignUser(val:any): Observable<any>{
    return this.http.get(Url+'getforeignuser/'+val);
  }

  sendMessage(val:any): Observable<any>{
    return this.http.post(Url+'sendmessage/', val);
  }

  viewMessage(sender: any, receiver: any): Observable<any> {
    return this.http.get(Url+'viewmessage/'+ sender + '/' + receiver);
  }
}
