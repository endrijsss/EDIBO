import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { MatDividerModule } from '@angular/material/divider';
import { MatSliderModule } from '@angular/material/slider';
import { MatIconModule } from '@angular/material/icon';
import { MatListModule } from '@angular/material/list';
import { MatButtonModule } from '@angular/material/button';
import { MatTabsModule } from '@angular/material/tabs';
import { MatTableModule } from '@angular/material/table';

import { ButtonOverviewExample } from './Buttons/button-overview-example';
import { TableBasicExample } from './Table/table-basic-example';
import {TablePaginationExample} from './app/table-pagination-example';

import { SomeService } from './app/some.service';

@NgModule({
  declarations: [
    AppComponent,
    ButtonOverviewExample,
    TableBasicExample,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatSliderModule,
    MatDividerModule,
    MatIconModule,
    MatListModule,
    MatButtonModule,
    MatTabsModule,
    MatTableModule,
  ],
  entryComponents: [TablePaginationExample],
  bootstrap: [AppComponent],
})
export class AppModule { }
