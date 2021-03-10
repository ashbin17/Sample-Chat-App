import { Component, OnInit } from '@angular/core';
import { TokenStorageService} from 'src/app/token-storage.service';
import { ServiceService} from 'src/app/service.service';
import { Router} from '@angular/router';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})


export class ProfileComponent implements OnInit {

  currentUser: any;
  logindetail: any;
  filepath: any;
  param = 0
  //token_val: any;

  constructor(private token: TokenStorageService, private service: ServiceService, private router:Router) { }

  ngOnInit(): void {
    /*this.activatedRoute.params.subscribe(data => {
      this.param = data.id;
    });*/
    this.param = this.token.getprofile();
    if(this.param == undefined){
      this.currentuser();
    }
    if(this.param > 0){
      this.foreignuser(this.param);
    }
  
  }

  currentuser(): void{
    this.service.getCurrentUser().subscribe(response =>{
      this.currentUser = response;
      this.filepath = this.currentUser.pic;
    },
    error => {
      this.router.navigate(['userdetail']);
    });
    //this.token_val = this.token.getToken();
    //console.log(this.token_val);

    this.service.getUserDetails().subscribe(response => {
      this.logindetail = response;
    })
  }

  foreignuser(id:number):void {
    this.service.getForeignUser(this.param).subscribe(response => {
      this.currentUser = response.details_serializer;
      this.filepath = this.currentUser.pic;
      this.logindetail = response.user_serializer;
    },
    error =>{
      console.log(error);
    });
  }

}
