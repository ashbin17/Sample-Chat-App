import { Component, OnInit } from '@angular/core';
import { ServiceService } from 'src/app/service.service'

@Component({
  selector: 'app-userdetail',
  templateUrl: './userdetail.component.html',
  styleUrls: ['./userdetail.component.css']
})
export class UserdetailComponent implements OnInit {

  isdetails = false;
  photofilename: any;
  photofilepath: any;
  PhotoUrl = "http://127.0.0.1:8000/media/"
  form: any ={
    nickname: '',
    phone: '',
    dob: '',
    language: '',
    pic: ''
  }

  constructor(private service: ServiceService) { }

  ngOnInit(): void {
    this.service.getCurrentUser().subscribe(response => {
        this.form = response;
        this.photofilepath = this.form.pic;
    },
    error => {
      this.isdetails = true;
    });
  }


  adduserdetails(){
    this.service.addUserDetails(this.form).subscribe(response => {
      console.log(response)
    });
    this.reloadPage();
  }

  edituserdetails(){
    this.service.edituserdetails(this.form).subscribe(response => {
      console.log(response);
    });
    this.reloadPage();
  }

  reloadPage(): void {
    window.location.reload();
  }

  uploadPhoto(event: any){
    var file=event.target.files[0];
    const formData:FormData=new FormData();
    formData.append('uploadedFile',file,file.name);

    this.service.UploadPhoto(formData).subscribe((data:any)=>{
      this.photofilename=data.toString();
      this.photofilepath = this.PhotoUrl+this.photofilename;
      this.form.pic = this.photofilepath;
    })
  }

}
