import { Component, OnInit } from '@angular/core';
import { ServiceService} from 'src/app/service.service';
import { AuthService} from 'src/app/auth.service';
import { TokenStorageService} from 'src/app/token-storage.service';
import { Router} from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  form: any = {
    username: null,
    password: null
  };

  isLoggedIn = false;
  isLoginFailed = false;
  errorMessage = '';
  roles: string[] = [];
  user = '';
  person :any;

  constructor(private authservice: AuthService, private tokenStorage: TokenStorageService, private service: ServiceService, private router:Router ) { }

  ngOnInit(): void {
    if (this.tokenStorage.getToken()) {
      this.isLoggedIn = true;
      this.roles = this.tokenStorage.getUser().roles;
      this.service.getUserDetails().subscribe(response =>{
        this.person = response;
      });
      this.router.navigate(['home']);
    }
  }

  onSubmit(): void {
    const { username, password } = this.form;
    console.log();

    this.authservice.login(username, password).subscribe(response => {
      console.log(response);
      this.tokenStorage.saveToken(response.token);
      this.tokenStorage.saveUser(response);

      this.isLoginFailed = false;
      this.isLoggedIn = true;
      this.roles = this.tokenStorage.getUser().roles;

      //this.service.getUserDetails()
      this.reloadPage();
      //this.router.navigate(['home']);
      
    },
    err => {
      console.error();
      this.errorMessage = err.error.message;
      this.isLoginFailed = true;
    });
  }

  reloadPage(): void {
    window.location.reload();
  }

}
