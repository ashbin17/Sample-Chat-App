import { Component, OnInit } from '@angular/core';
import { TokenStorageService} from 'src/app/token-storage.service';
import { ServiceService} from 'src/app/service.service';

@Component({
  selector: 'app-users',
  templateUrl: './users.component.html',
  styleUrls: ['./users.component.css']
})
export class UsersComponent implements OnInit {

  users:any;
  details: any;
  searchtext:string="";
  searchwork = true;

  constructor(private service: ServiceService) { }

  ngOnInit(): void {

    this.service.getAllUser().subscribe(response => {
      this.users = response.user_serializer;
      this.details = response.details_serializer;
    },
    error =>{
      console.log(error);
    });
  }

  search1(){
    if (this.searchtext){
      this.search();
    }
    else{
      window.location.reload();
    }
  }
  search(){
   
    this.service.search(this.searchtext).subscribe(data => {
      console.log(data);
      this.users = data.user_serializer;
      this.details = data.details_serializer;
      this.searchwork = true;
    },
    error => {
      console.log(error);
      this.searchwork = false;
    });
  }

}
