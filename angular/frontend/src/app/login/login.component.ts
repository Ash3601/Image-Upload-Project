import { HttpClient } from '@angular/common/http';
import { Component, OnInit  } from '@angular/core';
import {FormGroup, FormControl} from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  profiles: any;
 constructor(private http: HttpClient, private router: Router) {
 }

 ngOnInit() {}

 loginForm = new FormGroup({
  uname: new FormControl(),
  pwd: new FormControl()
 })


 checkUser(event:any) {
    this.http.get('http://127.0.0.1:8000/profiles/').subscribe(
      data => {
        this.profiles = JSON.parse(JSON.stringify(data));
         let currentUser:any = event.target['uname'].value;
         let currentUserPwd = event.target['pwd'].value;
         for (let profile of this.profiles) {
          if (currentUser === profile.user && currentUserPwd === profile.pwd) {
              localStorage.setItem('user', currentUser);
              this.router.navigateByUrl('/home')
          }
        }
        },
      error => console.log(error)
    );
 }
}
