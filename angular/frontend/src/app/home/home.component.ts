import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {
  title: string = '';
  image: any;
  description: string = '';
  user: any = localStorage.getItem('user');

  constructor(private http: HttpClient, private router: Router) {}

  onTitleChanged(event: any) {
    this.title = event.target.value;
  }

  onImageChanged(event: any) {
    this.image = event.target.files[0];
  }

  onDescriptionChanged(event: any) {
    this.description = event.target.value;
  }
  newBook() {
    this.user = localStorage.getItem('user');
    console.log('Book function called')
    const uploadData = new FormData();
    uploadData.append('title', this.title);
    uploadData.append('description', this.description);
    uploadData.append('user', this.user);
    uploadData.append('image', this.image, this.image.name);
    this.http.put('http://127.0.0.1:8000/images/', uploadData).subscribe(
      data => console.log(data),
      error => console.log(error)
    );
  }

  images:any = [];

  getBook() {
    console.log('Book function called get')
    this.http.get('http://127.0.0.1:8000/images/').subscribe(
      data => {console.log(JSON.stringify(data)); this.images = JSON.parse(JSON.stringify(data)); console.log(typeof(JSON.stringify(data))); console.log(this.images.length);},
      error => console.log(error)
    );
  }

  logout() {
    localStorage.removeItem('user');
    this.router.navigateByUrl('/login');
  }
}
