import { Component, OnInit } from '@angular/core';
import { ServiceService} from 'src/app/service.service';
import { AuthService} from 'src/app/auth.service';
import { Router} from '@angular/router';

@Component({
  selector: 'app-registration',
  templateUrl: './registration.component.html',
  styleUrls: ['./registration.component.css']
})
export class RegistrationComponent implements OnInit { 

  usr:any = {
    email: '',
    username: '',
    password: ''

  };

  constructor(private service: AuthService, private router:Router) { }

  ngOnInit(): void {
  }

  register(){
    const person = {
      email: this.usr.email,
      username: this.usr.username,
      password: this.usr.password
    }
    this.service.register(person.username, person.email, person.password).subscribe(response => {
      console.log(response)
    },
    error =>{
      console.error();
    });

    this.router.navigate(['login']);
  }

}
