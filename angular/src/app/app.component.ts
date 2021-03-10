import { Component, OnInit } from '@angular/core';
import { TokenStorageService} from 'src/app/token-storage.service';
import { ServiceService} from 'src/app/service.service';
import { Router} from '@angular/router'

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  private roles: string[] = [];
  isLoggedIn = false;
  showAdminBoard = false;
  showModeratorBoard = false;
  person:any;

  constructor(private tokenStorageService: TokenStorageService, private service: ServiceService, private router: Router) { }

  ngOnInit(): void {
    this.isLoggedIn = !!this.tokenStorageService.getToken();

    if (this.isLoggedIn) {
      const user = this.tokenStorageService.getUser();
      this.service.getUserDetails().subscribe(response =>{
        this.person = response;
      });
      /*this.roles = user.roles;

      this.showAdminBoard = this.roles.includes('ROLE_ADMIN');
      this.showModeratorBoard = this.roles.includes('ROLE_MODERATOR');*/

    }
    else{
      this.router.navigate(['login'])
    }
  }

  logout(): void {
    this.tokenStorageService.signOut();
    window.location.reload();
  }
  title = 'authui';
}
