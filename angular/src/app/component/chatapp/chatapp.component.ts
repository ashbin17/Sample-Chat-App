import { Component, OnInit, ViewChild, ElementRef, AfterViewInit } from '@angular/core';
import {TokenStorageService} from 'src/app/token-storage.service';
import {ServiceService} from 'src/app/service.service'

@Component({
  selector: 'app-chatapp',
  templateUrl: './chatapp.component.html',
  styleUrls: ['./chatapp.component.css']
})
export class ChatappComponent implements OnInit {

  msg: any = {
    msg: '',
    sender: '',
    receiver: ''
  };

  viewmsg: any;
  sender: any;
  receiver: any;
  receiver_img: any;
  sender_img: any;

  constructor(private token: TokenStorageService, private service: ServiceService) { }

  ngOnInit(): void {
    this.receiver = this.token.getprofile();
    
    if(this.receiver){
      this.getreceiver();
    }

  }

  getreceiver(){
    this.service.getForeignUser(this.receiver).subscribe(response => {
      this.receiver = response.user_serializer;
      this.receiver_img = response.details_serializer.pic;
      this.getsender();
    });
  }

  getsender(){
    this.service.getUserDetails().subscribe(response => {
      this.sender = response;
      this.service.getCurrentUser().subscribe(response => {
        this.sender_img = response.pic;
      })
      this.view_message();
    });
  }

  send(){
    this.msg.sender = this.sender.id;
    this.msg.receiver = this.receiver.id;
    if (this.msg.msg){
      this.service.sendMessage(this.msg).subscribe(response => {
        console.log(response);
      },
      error => {
        console.log(error);
      });
      
      window.location.reload();
    }
  }

  view_message(){
    this.service.viewMessage(this.sender.id, this.receiver.id).subscribe(response => {
      this.viewmsg = response;
    },
    error => {
      console.log(error);
    });
  }

}
